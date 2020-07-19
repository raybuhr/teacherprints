// set the dimensions and margins of the graph
var margin_t = {top: 0, right: 10, bottom: 70, left: 10},
    width_t = 650 - margin_t.left - margin_t.right,
    height_t = 150 - margin_t.top - margin_t.bottom;

// append the svg object to the body of the page
var svg_t = d3.select("#tapestry")
  .append("svg")
    .attr("width", width_t + margin_t.left + margin_t.right)
    .attr("height", height_t + margin_t.top + margin_t.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin_t.left + "," + margin_t.top + ")");

// Initialize the X axis
var x_t = d3.scaleLinear()
  .range([ 0, width_t ]);
var xAxis_t = svg_t.append("g")
  .attr("transform", "translate(0," + height_t/2 + ")")

// Initialize the Y axis
var y_t = d3.scaleLinear()
  .range([ height_t, 0]);
var yAxis_t = svg_t.append("g")
  .attr("class", "myYaxis")

// Parse the Data 
  d3.csv("https://raw.githubusercontent.com/TSSlade/teacherprints/anna-branch/TestData/CSV/tz_swahili.csv?token=AILF2SLIZP4QWD5RHRMJTQK7DTBLI", function(data) 
       
{
    // X axis
    x_t.domain([0, d3.max(data, function(d) { return +d.START + 1; })] );
      
    // Add Y axis
    y_t.domain([-d3.max(data, function(d) { return Math.abs(parseFloat(d['COUNT'])); }), d3.max(data, function(d) { return Math.abs(parseFloat(d['COUNT'])); })]);
        
    // variable u: map data to existing line
    var t = svg_t.selectAll(".myLine")
      .data(data)
    // update lines
    t
      .enter()
      .append("line")
      .attr("class", "myLine")
      .merge(t)
      .transition()
      .duration(1000)
      .attr("x1", function(d) { return x_t(d.START) + x_t(d.DUR)/2; })
      .attr("x2", function(d) { return x_t(d.START) + x_t(d.DUR)/2; })
      .attr("y1", function(d) {
        if(d.LABEL == "CHILD") { return y_t(0);}
          else {return y_t(d['COUNT'])}
      ;})
      .attr("y2", function(d) { 
        if(d.LABEL == "CHILD") { return y_t(d['COUNT']);} 
          else { return y_t(0);}
      ;})
      .attr("stroke", function(d) { 
        if(d.LABEL == "CHILD") { return '#FDB515'} 
          else { return '#00B0DA'}
      ;})
      .attr("stroke-width", function(d) { return x_t(d.DUR); })
      .attr('opacity', 0.8)
    
     

    

  })