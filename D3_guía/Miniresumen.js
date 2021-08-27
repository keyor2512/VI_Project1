//Creación del svg principal "area de dibujo"
var svg = d3.select("body")
.append("svg")
.attr("height", alto)
.attr("width",ancho);

// agregar una linea
svg.append("line")
.attr("x1", 5)
.attr("x2", ancho -5)
.attr('y1', 35)
.attr("y2", 35)
//Color
.attr('stroke', 'black')
//ancho
.attr('stroke-width', 1)

//factor de escalado (convierte los valores grandes a valores que entren en pantalla)
var escalaY = d3.scaleLinear()
              //El dominio es el valor minimo y maximo que se obtendrá de los datos
              .domain([100000,288054])
              //El rango en el que se dará la salida. No debe ser mayor al tamaño del svg
              .range([0, 400]);


//Escala de colores, esta página es muy útil https://github.com/d3/d3-scale#continuous_clamp
var escalaColores = d3.scaleOrdinal(d3.schemeRdYlGn[10])

d3.csv("placeholder.com" ,function(d){
  // Se convierten los datos a numeros
   d.numero1 = +d.numero1;
   d.numero2 = +d.numero2;

   return d})
   //Recoge todo los datos en un arreglo
   .then(function(datos){
	//Manipulación de los datos con los datos
});

//el svg creado en una variable.
svg.selectAll("rect")
     //se le pasa el un arreglo de datos
     .data(datos)
     //agrega los nuevos elementos
     .enter()
     //agrega un rectangulo
     .append("rect")
     //*** Todos los .attr modifica atributos de lo que se este agregando. ****
     //posición en x
     .attr("x", function(d,i){
       //calculo para espaciarlos. d es datos, i es indice.
       return i * (ancho -2 * (margen))/ 10;
     })
     //posición en y
     .attr("y", function(d){
       //utiliza la function de escalado para con los datos de la poblacion y le resta el tamaño
       //del svg, para hubicarlo al fondo( el rectangulo se dibuja de arriba a abajo).
       return (alto + 10) - escalaY(d.numero);
     })
     .attr("height", numero)
       .attr("width", numero)
     //relleno
     .attr("fill", function(d){
       //asocia el color a un valor
       return escalaColores(d.area)
     })
//reacciona a eventos
     .on("mouseover", function(){
        //codigo de lo que va a hacer
     }

//Elimina todos los rectangulos
svg.selectAll("rect")
       .remove();
