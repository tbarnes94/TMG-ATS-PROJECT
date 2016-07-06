$(document).ready(function() {

	// var request = new XMLHttpRequest();

	var dataList = document.getElementById('json-datalist');

	$.getJSON( "colleges.json").done(function( data ) {
		// console.log(data);
		// console.log(data[0]);
		data.forEach(function(college){
			var option = document.createElement('option');
			option.value = college;
			dataList.appendChild(option);
		});
	}).fail(function(xhr, status, error) {
		console.log(error);
	});
});