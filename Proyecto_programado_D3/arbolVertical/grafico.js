export default function define(runtime, observer,tipo) {
  const main = runtime.module();
  var cont = -1;
  var padre=0;
  var columnas=3;
  const fileAttachments = new Map([["sample.json",new URL("sample.json",import.meta.url)]]);
  main.builtin("FileAttachment", runtime.fileAttachments(name => fileAttachments.get(name)));

  main.variable(observer("chart")).define("chart", ["partition","data","d3","width","height","color","format"], function(partition,data,d3,width,height,color,format)
{
  var root = partition(data);
  if(tipo<0){
    columnas=3;
    root = partition(data);
    
  }
  else{
    columnas=2;
    root = partition(data.children[tipo]);
    
  }
  let focus = root;

  const svg = d3.create("svg")
      .attr("viewBox", [0, 0, width, height])
      .style("font", "10px sans-serif");

  const cell = svg
    .selectAll("g")
    .data(root.descendants())
    .join("g")
    .attr("transform", d => `translate(${getPosi(d)},${d.y0})`);

  const rect = cell.append("rect")
      .attr("width", d => getTam(d))
      .attr("height", d => rectHeight(d))
      .attr("fill-opacity", 0.6)

      .attr("fill", d => {
        if (!d.depth) return color("rgb(202,202,203)");
        while (d.depth > 1) d = d.parent;
        return color(d.data.name);
      });
      

  const text = cell.append("text")
      .style("user-select", "none")
      .style("writing-mode",d=>getStyle(d))
      .attr("x", 4)
      .attr("y", 13)

      .attr("fill-opacity", d => +labelVisible(d));

  text.append("tspan")
      .text(d => getText(d.data.name))

  const tspan = text.append("tspan")
      .attr("fill-opacity", d => labelVisible2(d))
      .text(d => ` ${format(d.value)}`);



  cell.append("title")
      .text(d => `${d.ancestors().map(d => d.data.name).reverse().join("/")}\n${format(d.value)}`);
  function getStyle(d){

      if((d.depth>1&&tipo<0)||(d.depth>0&&tipo>=0)){
        return "vertical-rl";
      }
      else{
        return "horizontal-tb";
      }
  }
  function labelVisible(d) {
    
    return d.y1 <= 975 && d.y0 >= 0 && d.x1 - d.x0 > 16;
  
  }
  function labelVisible2(d) {

   if(d.x1-d.x0>380){
    return 1;
    }
    else{
      return 0;
    }
  
  }
  function getPosi(d){

    if(d.depth==0){
      return d.x0;
    }
    else{
      if(d.parent!=padre){
        padre=d.parent
        cont=-1;
      }
      cont=cont+1
      d.x0=((d.parent.x1-d.parent.x0)/(d.parent.children.length-1)*cont)+d.parent.x0;
      d.x1=d.x0+(d.parent.x1-d.parent.x0)/(d.parent.children.length-1);

      d=d.parent;

      

      return (((d.x1-d.x0)/(d.children.length-1))*cont)+d.x0
    }
  }
  
  function rectHeight(d) {
    return d.y1 - d.y0 - Math.min(1, (d.y1 - d.y0) / 2);
  }

  
  return svg.node();
}
);
  function getText(texto) {
    if(texto!=undefined){
    if(texto.length>40){
      return texto.substring(0,40)+"...";
    }
    else{
      return texto;
    }}
    else{
      return texto;
    }
  }
  function getCol(){

    return columnas;
  }
  function getTam(d){

    if(d.depth==0){
      d.y1= d.x1 - d.x0 - 1
      
      return  d.x1 - d.x0 - 1
    }
    else{


      d=d.parent;
      

      return (d.y1-d.y0)/(d.children.length-1)
    }
    
  }
  main.variable().define("data", ["FileAttachment"], function(FileAttachment){return(
FileAttachment("sample.json").json()
)});
  main.variable().define("partition", ["d3","height","width"], function(d3,height,width){return(
data => {
  const root = d3.hierarchy(data)
      .sum(d => d.value)
      .sort((a, b) => b.height - a.height || b.value - a.value);  
  return d3.partition()
      .size([width, (root.height + 1) * height /getCol()])
    (root);
}
)});
  main.variable().define("color", ["d3","data"], function(d3,data){return(
d3.scaleOrdinal(d3.quantize(d3.interpolateBlues, data.children.length + 1))
)});
  main.variable().define("format", ["d3"], function(d3){return(
d3.format(",d")
)});
  main.variable().define("width", function(){return(
975
)});
  main.variable().define("height", function(){return(
400
)});
  main.variable().define("d3", ["require"], function(require){return(
require("d3@6")
)});
  return main;
}
