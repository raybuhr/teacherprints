// set the dimensions and margins of the graph
var margin = { top: 10, right: 95, bottom: 60, left: 65 },
  width = 550 - margin.left - margin.right,
  height = 275 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3
  .select("#statements")
  .append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// define the data
var data = [
  {
    name: "TEACHER",
    value: 8.8
  },
  {
    name: "STUDENT",
    value: 1.4
  }
];

// Add X axis
var x = d3
  .scaleLinear()
  .domain([
    0,
    d3.max(data, function (d) {
      return d.value;
    })
  ])
  .range([0, width]);

svg.append("g").attr("transform", "translate(0," + height + ")");

// Y axis
var y = d3
  .scaleBand()
  .range([0, height])
  .domain(
    data.map(function (d) {
      return d.name;
    })
  )
  .padding(0.1);

//Bars
svg
  .selectAll("myRect")
  .data(data)
  .enter()
  .append("rect")
  .attr("x", x(0))
  .attr("y", function (d) {
    return y(d.name);
  })
  .attr("width", function (d) {
    return x(d.value);
  })
  .attr("height", y.bandwidth())
  .attr("fill", function (d) {
    if (d.name == "STUDENT") {
      return "#FDB515";
    } else {
      return "#00B0DA";
    }
  });

//Name Labels
svg
  .selectAll("allLabels")
  .data(data)
  .enter()
  .append("text")
  .text(function (d) {
    return d.name;
  })
  .attr("x", function (d) {
    return x(0) - 10;
  })
  .attr("y", function (d) {
    return y(d.name) + y.bandwidth()/2;
  })
  .attr("text-anchor", "end")
  .attr("font-size", "10px")
  .attr("fill", "black");

//Name Labels
svg
  .selectAll("allLabels")
  .data(data)
  .enter()
  .append("text")
  .text("AVERAGE")
  .attr("x", function (d) {
    return x(0) - 10;
  })
  .attr("y", function (d) {
    return y(d.name) + y.bandwidth()/2 - 15;
  })
  .attr("text-anchor", "end")
  .attr("font-size", "10px")
  .attr("fill", "black");

//Name Labels
svg
  .selectAll("allLabels")
  .data(data)
  .enter()
  .append("text")
  .text("STATEMENT")
  .attr("x", function (d) {
    return x(0) - 10;
  })
  .attr("y", function (d) {
    return y(d.name) + y.bandwidth()/2 + 15;
  })
  .attr("text-anchor", "end")
  .attr("font-size", "10px")
  .attr("fill", "black");


//Value Labels
svg
  .selectAll("allLabels")
  .data(data)
  .enter()
  .append("text")
  .text(function (d) {
    return d.value  + " sec";
  })
  .attr("x", function (d) {
    return x(d.value) + 10;
  })
  .attr("y", function (d) {
    return y(d.name) + y.bandwidth()/2 + 5;
  })
  .attr("text-anchor", "start")
  .attr("font-size", "24px")
  .attr("font-weight", "bold")
  .attr("fill", "#888888");
