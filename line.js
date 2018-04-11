var lineChart = function(workload, timestampList) {
    var container = '<div id="workloadDropdown"></div><div id="linesgraphs"><div class="row"><div class="column"><div id="graph1"><div id="apache"></div></div><div id="tomcat"></div></div></div><div class="row"><div class="column"><div id="cdjb"></div><div id="mysql"></div></div></div></div>'
    document.getElementById("linegraphs").innerHTML(container); 
    console.log(workload)
    timestamp_min = timestampList[0]
    timestam_max = timestampList[timestampList.length - 1]

    var margin = {top: 20, right: 20, bottom: 110, left: 40},
    margin2 = {top: 430, right: 20, bottom: 30, left: 40},
    width = 950, 
    height = 500

    d3.select("graph1").append("svg")
        .attr("width", width)
        .attr("height", height)

    height2 = height


    var x = d3.scaleTime().range([0, width - margin.left - margin.bottom]),
        x2 = d3.scaleTime().range([0, width - margin.left- margin.bottom]),
        y = d3.scaleLinear().range([height - margin.top - margin.right, 0]),
        y2 = d3.scaleLinear().range([height2 - margin.top - margin.right, 0]);

    var xAxis = d3.axisBottom(x),
        xAxis2 = d3.axisBottom(x2),
        yAxis = d3.axisLeft(y);

    var brush = d3.brushX()
        .extent([[0, 0], [width, height2]])
        .on("brush end", brushed);

    var zoom = d3.zoom()
        .scaleExtent([1, Infinity])
        .translateExtent([[0, 0], [width, height]])
        .extent([[0, 0], [width, height]])
        .on("zoom", zoomed);   
}