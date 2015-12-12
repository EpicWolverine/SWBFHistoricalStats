loadJSON(function(response) {
        // Do Something with the response e.g.
        populateGraph(JSON.parse(response));

        // Assuming json data is wrapped in square brackets as Drew suggests
        //console.log(jsonresponse[0].name);
});

function loadJSON(callback) {
    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', 'data.json', true);
    xobj.onreadystatechange = function () {
        if (xobj.readyState == 4 && xobj.status == "200") {
            // .open will NOT return a value but simply returns undefined in async mode so use a callback
            callback(xobj.responseText);
        }
    }
    xobj.send(null);
}

function populateGraph(json){
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
        multiTooltipTemplate: "<%= datasetLabel %> - <%= value %>",
        pointDot : false,
        pointDotRadius : 2,
        pointHitDetectionRadius : 8
    });
};