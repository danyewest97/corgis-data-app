window.onload = function () {
	var chart = new CanvasJS.Chart("chartContainer", {
		theme: "light2", // "light1", "light2", "dark1", "dark2"
		animationEnabled: true,
		zoomEnabled: true,
		title: {
			text: "Wind Turbine Growth in " + $("#data").data("state") + " Over Time"
		},
		axisX: {
			title: "Year",
			valueFormatString: "####"
		},
		axisY: {
			title: "Number of Turbines Built",
			includeZero: false,
		},
		toolTip: {
			contentFormatter: function (e) {
               return e.entries[0].dataPoint.x + ": " + e.entries[0].dataPoint.y + " turbines";  
			} 
		},
		data: [{
			type: "column",
			dataPoints: []
		}]
	});
	
	
	JSONData = $("#data").data("points");
	chart.options.data[0].dataPoints = JSONData;
	chart.render();
	
}