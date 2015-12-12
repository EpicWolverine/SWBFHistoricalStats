var json = [
{"timestamp":"2015/12/11 21:50:28","pc":"16585","xboxone":"46381","ps4":"87683","total":"150649"},
{"timestamp":"2015/12/11 21:55:28","pc":"16518","xboxone":"46615","ps4":"88014","total":"151147"},
{"timestamp":"2015/12/11 22:00:28","pc":"16468","xboxone":"47075","ps4":"88184","total":"151727"}
];;

var timestamps = [];
var pc = [];
var xboxone = [];
var ps4 = [];
var total = [];

for (var i = 0; i < json.length; i++) {
    timestamps.push(json[i].timestamp);  
}
for (var i = 0; i < json.length; i++) {
    pc.push(json[i].pc);  
}
for (var i = 0; i < json.length; i++) {
    xboxone.push(json[i].xboxone);  
}
for (var i = 0; i < json.length; i++) {
    ps4.push(json[i].ps4);  
}
for (var i = 0; i < json.length; i++) {
    total.push(json[i].total);  
}

var chartData = {
            labels : timestamps,
            datasets : [
                {
                    label: "PC",
                    fillColor : "rgba(255,211,6,0.7)",
                    strokeColor : "rgba(255,211,6,0.9)",
                    pointColor: "rgba(255,211,6,1)",
                    pointStrokeColor: "#ffffff",
                    pointHighlightFill: "#ffffff",
                    pointHighlightStroke: "rgba(255,211,6,1)",
                    data : pc
                },
                {
                    label: "Xbox One",
                    fillColor : "rgba(93,194,30,0.3)",
                    strokeColor : "rgba(16,124,16,0.9)",
                    pointColor: "rgba(16,124,16,1)",
                    pointStrokeColor: "#ffffff",
                    pointHighlightFill: "#ffffff",
                    pointHighlightStroke: "rgba(16,124,16,1)",
                    data : xboxone
                },
                {
                    label : "PS4",
                    fillColor : "rgba(0,55,145,0.3)",
                    strokeColor : "rgba(0,55,145,0.9)",
                    pointColor: "rgba(0,55,145,1)",
                    pointStrokeColor: "#ffffff",
                    pointHighlightFill: "#ffffff",
                    pointHighlightStroke: "rgba(0,55,145,1)",
                    data : ps4
                },
                {
                    label : "Total",
                    fillColor : "rgba(127,127,127,0.2)",
                    strokeColor : "rgba(0,0,0,0.9)",
                    pointColor: "rgba(0,0,0,1)",
                    pointStrokeColor: "#ffffff",
                    pointHighlightFill: "#ffffff",
                    pointHighlightStroke: "rgba(0,0,0,1)",
                    data : total
                }
            ]
        };
var lineChart = new Chart(document.getElementById("canvas").getContext("2d")).Line(chartData, {
    multiTooltipTemplate: "<%= datasetLabel %> - <%= value %>"
});