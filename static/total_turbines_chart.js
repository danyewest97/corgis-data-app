window.onload = function() {

var chart = new CanvasJS.Chart("chartContainer", {
	theme: "light2", // "light1", "light2", "dark1", "dark2"
	exportEnabled: true,
	animationEnabled: true,
	title: {
		text: "Wind Turbines Across the US"
	},
	data: [{
		type: "pie",
		startAngle: 25,
		toolTipContent: "<b>{label}</b>: {y}%",
		showInLegend: "false",
		legendText: "{label}",
		indexLabelFontSize: 16,
		indexLabel: "{label} - {y}%",
		dataPoints: [
			{ y: 9.2, label: "IA" },
			{ y: 0.1, label: "MA" },
			{ y: 0.6, label: "OH" },
			{ y: 4.1, label: "MN" },
			{ y: 5.1, label: "IL" },
			{ y: 1.9, label: "NE" },
			{ y: 2.0, label: "WY" },
			{ y: 5.4, label: "KS" },
			{ y: 6.4, label: "CA" },
			{ y: 1.2, label: "PA" },
			{ y: 25.5, label: "TX" },
			{ y: 2.3, label: "IN" },
			{ y: 0.2, label: "NC" },
			{ y: 2.3, label: "NM" },
			{ y: 0.1, label: "NH" },
			{ y: 2.2, label: "MI" },
			{ y: 7.1, label: "OK" },
			{ y: 1.8, label: "NY" },
			{ y: 3.3, label: "ND" },
			{ y: 1.9, label: "SD" },
			{ y: 4.2, label: "CO" },
			{ y: 0.2, label: "HI" },
			{ y: 0.1, label: "NJ" },
			{ y: 0.6, label: "WV" },
			{ y: 3.2, label: "OR" },
			{ y: 0.2, label: "AK" },
			{ y: 2.8, label: "WA" },
			{ y: 1.0, label: "MT" },
			{ y: 0.6, label: "ME" },
			{ y: 0.1, label: "RI" },
			{ y: 0.7, label: "WI" },
			{ y: 1.4, label: "MO" },
			{ y: 0.1, label: "VT" },
			{ y: 0.1, label: "TN" },
			{ y: 0.8, label: "ID" },
			{ y: 0.3, label: "UT" },
			{ y: 0.1, label: "VA" },
			{ y: 0.1, label: "MD" },
			{ y: 0.4, label: "AZ" },
			{ y: 0.1, label: "PR" },
			{ y: 0.1, label: "GU" },
			{ y: 0.1, label: "NV" },
			{ y: 0.1, label: "DE" },
			{ y: 0.1, label: "CT" }
		]
	}]
});
chart.render();

}