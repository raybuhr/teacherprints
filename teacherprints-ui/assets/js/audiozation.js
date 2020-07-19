// set the dimensions and margins of the graph
var margin = {top: 10, right: 10, bottom: 70, left: 10},
    width = 650 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#audiozation")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

// Initialize the X axis
var x = d3.scaleLinear()
  .range([ 0, width ]);
var xAxis = svg.append("g")
  .attr("transform", "translate(0," + height/2 + ")")

// Initialize the Y axis
var y = d3.scaleLinear()
  .range([ height, 0]);
var yAxis = svg.append("g")
  .attr("class", "myYaxis")


// Parse the Data 
  d3.csv("https://raw.githubusercontent.com/TSSlade/teacherprints/anna-branch/TestData/CSV/tz_swahili.csv?token=AILF2SLIZP4QWD5RHRMJTQK7DTBLI", function(data) 

{
    // X axis
    x.domain([0, d3.max(data, function(d) { return +d.START + 20; })] );
  xAxis.transition().duration(1000).call(d3.axisBottom(x))
      
    // Add Y axis
    y.domain([-d3.max(data, function(d) { return Math.abs(parseFloat(d['LABEL_NUM'])); }), d3.max(data, function(d) { return Math.abs(parseFloat(d['LABEL_NUM'])); })]);
        
    // variable u: map data to existing line
    var j = svg.selectAll(".myLine")
      .data(data)
    // update lines
    j
      .enter()
      .append("line")
      .attr("class", "myLine")
      .merge(j)
      .transition()
      .duration(1000)
      .attr("x1", function(d) { return x(d.START) + x(d.DUR)/2; })
      .attr("x2", function(d) { return x(d.START) + x(d.DUR)/2; })
      .attr("y1", function(d) {
        if(d.LABEL == "CHILD") { return y(0);}
          else {return y(d['LABEL_NUM'])}
      ;})
      .attr("y2", function(d) { 
        if(d.LABEL == "CHILD") { return y(d['LABEL_NUM']);} 
          else { return y(0);}
      ;})
      .attr("stroke", function(d) { 
        if(d.LABEL == "CHILD") { return '#FDB515'} 
          else { return '#00B0DA'}
      ;})
      .attr("stroke-width", function(d) { return x(d.DUR); })
      .attr('opacity', .5)
    
      // variable u: map data to existing circle
    var v = svg.selectAll("circle")
      .data(data)
    // update circles
    v
      .enter()
      .append("circle")
      .merge(v)
      .transition()
      .duration(1000)
      .attr("cx", function(d) { return x(d.START) + x(d.DUR)/2; })
      .attr("cy", function(d) { 
        if(d.LABEL == "CHILD") { return y(d['LABEL_NUM']); }
          else { return y(d['LABEL_NUM']); }
      ;})
      .attr("r", function(d) { return x(d.DUR)/2; })
      .style("stroke", "black")
      .attr("stroke-width",0.5)
      //.attr("fill", "black")
      .attr("fill", function(d) { 
        if(d.LABEL == "CHILD") { return '#FDB515'} 
          else { return '#00B0DA'}
      ;})
      .attr('opacity', 1)    

  })





