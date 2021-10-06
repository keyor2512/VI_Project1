//
// Libreria Minim
//
import ddf.minim.*;

//
// Constantes
//
String cancion = "prueba5.mp3"; 
Minim minim;
color c;
PVector distance;
PFont sourcecode;

AudioPlayer song;             // Cancion a reproducirse.
AudioInput in;

int linesX = 40;              // numero de lineas en la direcion x.
int linesY = 26;              // numero de lineas en la direcion y.

int coef = 1;
int mode = 0;
float magnitude = 0;
float maxMagnitude = 848.5281374;

boolean lerping = true;
boolean repel = true;
boolean autopilot = false;
boolean controls = true;
boolean voice = false;

float stepsX, stepsY, radius, intensity, movement, last_sum, scale, factor, wave, sum;

//
// Clase nodo.
//
class Node {
  //
  // Solo tiene un constructor con las dimensiones y caracteristicas de la cancion.
  //
  float xpos, ypos, speed, anchorx, anchory;
  Node (float x, float y, float s) {
    anchorx = x;
    anchory = y;
    ypos = y;
    xpos = x;
    speed = s;
  }
}

//
// Instancio la matriz de nodos.
//
Node[][] Nodes = new Node[linesX][linesY];

//
// Clase captura
//
class Fish {
  //
  // Constructor con el x, y junto con la velocidad en que se detecta la cancion.
  //
  float xpos, ypos, speed;
  Fish () {
    ypos = random(800*0.25, 800*0.75);
    xpos = random(1000*0.25, 1000*0.75);
  }

  //
  // Actualiza el movimiento junto cno el volumen de la cancion.
  //
  void update() {
    if (lerping) {
      xpos = lerp(xpos + random(sum/20) - sum/40, xpos, 0.5);
      ypos = lerp(ypos + random(sum/20) - sum/40, ypos, 0.5);
    } else {
      xpos = xpos + random(sum/20) - sum/40;
      ypos = ypos + random(sum/20) - sum/40;
    }
    if (ypos > height*0.75) {
      ypos = height*0.75;
    } else if (xpos > width*0.75) {
      xpos = width*0.75;
    } else if (xpos < width*0.25) {
      xpos = width*0.25;
    } else if (ypos < height*0.25) {
      ypos = height*0.25;
    }
  }
}

//
// Instancion la captura de la cancion que se este reproducion.
//
Fish comportamiento_cancion = new Fish();

void setup() {
  fullScreen();
  noSmooth();
  colorMode(HSB, 255);
  stepsX = (width) / linesX;
  stepsY = (height) / linesY;

  for (int i = 0; i < linesX; i++) {
    for (int j = 0; j < linesY; j++) {
      Nodes[i][j] = new Node((i+0.5)*stepsX, (j+0.5)*stepsY, 2); //Se setea nodo
    }
  }
  minim = new Minim(this);
  song = minim.loadFile(cancion);
  in = minim.getLineIn(Minim.MONO, 1024);
  song.play(73*1000+500);
  factor = float(width)/song.bufferSize();
  textAlign(LEFT);
  sourcecode = createFont("sourcecode.ttf", 100);
}

//
// Accion de apretar tecla en el teclado.
//
void keyPressed() {
  switch(key) {
  case ' ':
    repel = !repel;
    break;
  case 'm':
    mode += 1;
    if (mode > 1) {
      mode = 0;
    }
    break;
  case 'a':
    autopilot = !autopilot;
    break;
  case 's':
    saveFrame("wavepttrn-####.jpg");
    break;
  case 'h':
    controls = !controls;
    break;
  case 'v':
    voice = !voice;
    if (!voice) {
      song.play();
    } else {
      song.pause();
    }
    break;
  }
}

//
// Dibujo en el marco donde visualiza el comportamiento de la matriz de nodos.
//
void draw() {
  background(frameCount%255, 255, 30);
  coef = (repel ? 1 : -1);

  if (lerping) {
    magnitude = lerp(sum, last_sum, 0.7)/2.5;
  } else {
    magnitude = last_sum;
  }
  wave = last_sum/2.5;

  for (int i = 0; i < linesX; i++) {
    for (int j = 0; j < linesY; j++) {  // Recorre matriz para trasar nodo por nodo en el marco de la interfaz.
      if (autopilot) {
        comportamiento_cancion.update();
        distance = new PVector(Nodes[i][j].xpos - comportamiento_cancion.xpos, Nodes[i][j].ypos - comportamiento_cancion.ypos);
      } else {
        distance = new PVector(Nodes[i][j].xpos - mouseX, Nodes[i][j].ypos - mouseY);
      }

      // Caracteristicas explicitas de la cancion.
      scale = (1/distance.mag())*magnitude;
      fill(255);
      intensity = pow(1 - distance.mag()/(maxMagnitude), 5) / 5;
      radius = (intensity*magnitude);

      // Seteo los nodos con nuevos datos, para ir construyendo el comportamiento.
      Nodes[i][j].xpos += coef*(distance.x*scale)/25;
      Nodes[i][j].ypos += coef*(distance.y*scale)/25;
      Nodes[i][j].xpos = lerp(Nodes[i][j].xpos, Nodes[i][j].anchorx, 0.05);
      Nodes[i][j].ypos = lerp(Nodes[i][j].ypos, Nodes[i][j].anchory, 0.05);
      
      if (radius > 50) {
        radius = 50;
      }
      if (radius < 2) {
        radius = 2;
      }
      
      // Factores para mostrar en interfaz.
      c = color(170 + magnitude/2, magnitude*5, 255, 255);
      fill(c);
      stroke(c);
      
      if (mode == 0) {
        ellipse(Nodes[i][j].xpos + coef*(distance.x*scale), Nodes[i][j].ypos + coef*(distance.y*scale), radius, radius);
      }
      if (mode == 1) {
        strokeWeight(radius/3);
        strokeCap(PROJECT);
        line(Nodes[i][j].xpos + coef*(distance.x*scale), Nodes[i][j].ypos + coef*(distance.y*scale), Nodes[i][j].xpos, Nodes[i][j].ypos);
      }
    }
  }

  // Factores para mostrar en interfaz, como una ola del bit de la cancion.
  c = color(170 + wave/2, wave*5, 255, 255);
  fill(c);
  stroke(c);
  strokeWeight(2);
  
  sum = 0; //Incrementa la base sumada en la amplitud de la ola de sonido de la cancion.

  for (int i = 0; i < song.bufferSize() - 1; i++)
  {
    if (voice) {
      line(i*factor, height/2 + in.left.get(i)*last_sum + 2, i*factor+1, height/2 + in.left.get(i+1)*last_sum + 2);
      sum += abs(in.left.get(i));
    } else {
      line(i*factor, height/2 + song.left.get(i)*last_sum + 2, i*factor+1, height/2 + song.left.get(i+1)*last_sum + 2);
      sum += abs(song.left.get(i));
    }
  }
  last_sum = sum;

  // Control de HUD
  if (controls) {
    fill(255, 0, 255);
    textFont(sourcecode);
    textSize(18);
    text("[ espacio ] = alterar gravedad\n[ m ] = cambiar modo\n[ v ] = pausar cancion/modo de voz\n[ a ] = autopiloto\n[ s ] = guardar pantalla\n[ h ] = esconder controles", 20, 40);
  }
}
