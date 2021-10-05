import ddf.minim.*;


import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.BasicFileAttributeView;
import java.nio.file.attribute.BasicFileAttributes;
import java.nio.file.attribute.FileTime;
import java.text.SimpleDateFormat;


boolean repro=false;
boolean play=false;
boolean listo=false;
String cancion = "prueba5.mp3";
Minim minim;
File f;

AudioPlayer song;
AudioInput in;

boolean lerping = true;

int linesX = 40; // number of lines in x direction
int linesY = 26; // number of lines in y direction

boolean repel = true;
boolean autopilot = false;
boolean controls = true;
boolean voice = false;
int coef = 1;
int mode = 0;
float magnitude = 0;
float maxMagnitude = 848.5281374;

color c;
PVector distance;
PFont sourcecode;
float stepsX, stepsY, radius, intensity, movement, last_sum, scale, factor, wave, sum;
Node[][] Nodes = new Node[linesX][linesY]; // create matrix of Nodes
Fish jimmy = new Fish(); //create Jimmy



boolean view=false;
int cancionNum=0;





void setup(){
  fullScreen();
  
}
void draw(){
  if(!repro){
    fill(128,128,128);
    rect(0,0,width,height);
    fill(255, 255,255);
    rect(40, 10, 220, 40);
    rect(280, 15, 40, 30);
    textSize(50);
    fill(0, 4, 612);
    text("Canciones", 40, 45);
    textSize(20);
    text("Play", 282, 37);
    textSize(40);
    fill(255, 255,255);
    
    if (mousePressed && mouseX>40 && mouseX<40+220 &&
    mouseY>10 && mouseY<10+40) {
    view=!view;
    delay(100);
    
    }
    if (mousePressed && mouseX>280 && mouseX<280+40 &&
    mouseY>15 && mouseY<15+30 && listo) {
      repro=true;
    
    }
    if(view==true){
    menuDesp();
    }
  }
  else{
    if(!play){
      reproducir();
      play=true;
      f = new File(cancion);
    }
   
    
    
    dibrepro();
  }

}

int pressed(int Num){
  if(cancionNum==Num){
    return 100;
  }
  else{
    return 255;
  }
}

void menuDesp(){
  textSize(12);
  fill(pressed(1));
  rect(40, 80, 220, 40);
  
  fill(0,0,0);
  text("Fashion_Dance_Upbeat_Energy", 45, 105);
  if (mousePressed && mouseX>40 && mouseX<40+220 &&
  mouseY>80 && mouseY<80+40) {
  cancionNum=1;
  listo=true;
  cancion = "Fashion_Dance_Upbeat_Energy.mp3";
  delay(100);
}
  
  
  
  fill(pressed(2));
  rect(40, 130, 220, 40);
  fill(0,0,0);
  text("Latinas_feat._Vince_Miranda_-", 45, 155);
  if (mousePressed && mouseX>40 && mouseX<40+220 &&
  mouseY>130 && mouseY<130+40) {
  cancionNum=2;
  listo=true;
  cancion = "Latinas_feat._Vince_Miranda_-.mp3";
  delay(100);
}
  
  fill(pressed(3));
  rect(40, 180, 220, 40);
  fill(0,0,0);
  text("Melancholic_Piano__Harp_and_Strings", 45, 205);
  if (mousePressed && mouseX>40 && mouseX<40+220 &&
  mouseY>180 && mouseY<180+40) {
  cancionNum=3;
  listo=true;
  cancion = "Melancholic_Piano__Harp_and_Strings.mp3";
  delay(100);
}
  
  fill(pressed(4));
  rect(40, 230, 220, 40);
  fill(0,0,0);
  text("Mit-Rich_-_Electronic_Corporate", 45, 255);
  if (mousePressed && mouseX>40 && mouseX<40+220 &&
  mouseY>230 && mouseY<230+40) {
  cancionNum=4;
  listo=true;
  cancion = "Mit-Rich_-_Electronic_Corporate.mp3";
  delay(100);
}

  fill(pressed(5));
  rect(40, 280, 220, 40);
  fill(0,0,0);
  text("Year_of_Dreams_-_Soft_Inspiring", 45, 305);
  if (mousePressed && mouseX>40 && mouseX<40+220 &&
  mouseY>280 && mouseY<280+40) {
  cancionNum=5;
  listo=true;
  cancion = "Year_of_Dreams_-_Soft_Inspiring.mp3";
  delay(100);
}
}


class Node {
  float xpos, ypos, speed, anchorx, anchory;
  Node (float x, float y, float s) {
    anchorx = x;
    anchory = y;
    ypos = y;
    xpos = x;
    speed = s;
  }
}

class Fish {
  float xpos, ypos, speed;
  Fish () {
    ypos = random(800*0.25, 800*0.75);
    xpos = random(1000*0.25, 1000*0.75);
  }
  void update() {
    //increase movement w/ volume of song
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

void reproducir(){
  noSmooth();
  colorMode(HSB, 255);
  stepsX = (width) / linesX;
  stepsY = (height) / linesY;
  // initialize nodes
  for (int i = 0; i < linesX; i++) {
    for (int j = 0; j < linesY; j++) {
      Nodes[i][j] = new Node((i+0.5)*stepsX, (j+0.5)*stepsY, 2);
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

void dibrepro(){
 
  
  background(frameCount%255, 255, 30);
  coef = (repel ? 1 : -1);
  //movement = (abs(mouseX - pmouseX) + abs(mouseY- pmouseY));
  //magnitude = lerp(magnitude, movement, 0.1);
  //wave = 0;
  if (lerping) {
    magnitude = lerp(sum, last_sum, 0.7)/2.5;
  } else {
    magnitude = last_sum;
  }
  wave = last_sum/2.5;
  // draw nodes
  for (int i = 0; i < linesX; i++) {
    for (int j = 0; j < linesY; j++) {
      if (autopilot) {
        jimmy.update();
        distance = new PVector(Nodes[i][j].xpos - jimmy.xpos, Nodes[i][j].ypos - jimmy.ypos);
      } else {
        distance = new PVector(Nodes[i][j].xpos - mouseX, Nodes[i][j].ypos - mouseY);
      }
      scale = (1/distance.mag())*magnitude;
      fill(255);
      intensity = pow(1 - distance.mag()/(maxMagnitude), 5) / 5;
      radius = (intensity*magnitude);
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
  // draw wave code
  c = color(170 + wave/2, wave*5, 255, 255);
  fill(c);
  stroke(c);
  strokeWeight(2);
  sum = 0; //increase sum based on amplitude of wave
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

  // HUD controls
  if (controls) {
    fill(255, 0, 255);
    textFont(sourcecode);
    textSize(18);
    text("x = Cambiar cancion\n[ m ] = change mode\n[ v ] = Pausar\n"+f.getName()+"\n"+f.getAbsolutePath()+"\n", 20, 40);
    
  }
}

void keyPressed() {
  switch(key) {
  case 'x':
    song.pause();
    repro=false;
    play=false;
    listo=false;
    break;
  case 'm':
    mode += 1;
    if (mode > 1) {
      mode = 0;
    }
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
