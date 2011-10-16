$(document).ready(function() {
	var options = {
	   // dataType:   json,
		success:    processJson,
	};
	$('#editForm').ajaxForm(options);
});

function processJson(data) {
	if (data.status == 'ok') {
		$('#status').html("Information successfully updated.");
		$('#status').css({color: "green"});
	} else {
		$('#status').html("Updating error. Enter valid values.");
		$('#status').css({color: "red"});
	}
}

$(document).ajaxStart(function() { 
	$('#editForm input').attr("disabled", "disabled");
	$('#editForm textarea').attr("disabled", "disabled");
	$('#status').html("Sending form data...");
	$('#status').css({color: "blue"});
}).ajaxStop(function() {
	$('#editForm input').removeAttr("disabled");
	$('#editForm textarea').removeAttr("disabled");
});

