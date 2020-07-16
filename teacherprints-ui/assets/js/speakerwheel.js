// set the dimensions and margins of the graph
var width = 600;
height = 550;
margin = 100;

// The radius of the pieplot is half the width or half the height (smallest one). I subtract a bit of margin.
var radius = Math.min(width, height) / 2 - margin;

// append the svg object to the div called 'my_dataviz'
var svg = d3
  .select("#my_dataviz")
  .append("svg")
  .attr("width", width)
  .attr("height", height)
  .append("g")
  .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

// Create dummy data
var data = { TEACHER: 71, OVERLAPS: 3, STUDENT: 7, PAUSES: 19 };

// set the color scale
var color = d3
  .scaleOrdinal()
  .domain(data)
  .range(["#00B0DA", "#003262", "#FDB515", "#888888"]);

// Compute the position of each group on the pie:
var pie = d3
  .pie()
  .sort(null) // Do not sort group by size
  .value(function (d) {
    return d.value;
  });
var data_ready = pie(d3.entries(data));

// The arc generator
var arc = d3
  .arc()
  .innerRadius(radius * 0.4) // This is the size of the donut hole
  .outerRadius(radius * 1);

// The Student arc generator
var arcS = d3
  .arc()
  .innerRadius(radius * 1.02)
  .outerRadius(radius * 1.07);

// The Teacher arc generator
var arcT = d3
  .arc()
  .innerRadius(radius * 1.09)
  .outerRadius(radius * 1.14);

// Another arc that won't be drawn. Just for labels positioning
var outerArc = d3
  .arc()
  .innerRadius(radius * 1)
  .outerRadius(radius * 1);

// Build the pie chart: Basically, each part of the pie is a path that we build using the arc function.
svg
  .selectAll("allSlices")
  .data(data_ready)
  .enter()
  .append("path")
  .attr("d", arc)
  .attr("fill", function (d) {
    return color(d.data.key);
  })
  .attr("stroke", "black")
  .style("stroke-width", "0px")
  .style("opacity", 1);

svg
  .selectAll("allSlices")
  .data(data_ready)
  .enter()
  .append("path")
  .attr("d", arcT)
  .attr("fill", function (d) {
    if (d.data.key == "TEACHER") {
      return "#00B0DA";
    } else if (d.data.key == "OVERLAPS") {
      return "#00B0DA";
    } else {
      return "#FFFFFF";
    }
  })
  .attr("stroke", "black")
  .style("stroke-width", "0px")
  .style("opacity", 1);

svg
  .selectAll("allSlices")
  .data(data_ready)
  .enter()
  .append("path")
  .attr("d", arcS)
  .attr("fill", function (d) {
    if (d.data.key == "STUDENT") {
      return "#FDB515";
    } else if (d.data.key == "OVERLAPS") {
      return "#FDB515";
    } else {
      return "#FFFFFF";
    }
  })
  .attr("stroke", "black")
  .style("stroke-width", "0px")
  .style("opacity", 1);

// Add the polylines between chart and labels:
svg
  .selectAll("allPolylines")
  .data(data_ready)
  .enter()
  .append("polyline")
  .attr("stroke", "black")
  .style("fill", "none")
  .attr("stroke-width", 1)
  .attr("points", function (d) {
    var posA = arc.centroid(d); // line insertion in the slice
    var posB = outerArc.centroid(d); // line break: we use the other arc generator that has been built only for that
    var posC = outerArc.centroid(d); // Label position = almost the same as posB
    var midangle = d.startAngle + (d.endAngle - d.startAngle) / 2; // we need the angle to see if the X position will be at the extreme right or extreme left
    posC[0] = radius * 1.1 * (midangle < Math.PI ? 1 : -1); // multiply by 1 or -1 to put it on the right or on the left
    return [posA, posB, posC];
  });

// Add the polylines between chart and labels:
svg
  .selectAll("allLabels")
  .data(data_ready)
  .enter()
  .append("text")
  .text(function (d) {
    console.log(d.data.key);
    return d.data.key + " " + d.data.value + "%";
  })
  .attr("transform", function (d) {
    var pos = outerArc.centroid(d);
    var midangle = d.startAngle + (d.endAngle - d.startAngle) / 2;
    pos[0] = radius * 1.15 * (midangle < Math.PI ? 1 : -1);
    return "translate(" + pos + ")";
  })
  .style("text-anchor", function (d) {
    var midangle = d.startAngle + (d.endAngle - d.startAngle) / 2;
    return midangle < Math.PI ? "start" : "end";
  });

