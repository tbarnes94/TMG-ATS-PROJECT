function validatePhoneNumber(event) {
	var key = window.event ? event.keyCode : event.which;

	if (event.keyCode == 36 || event.keyCode == 9 || event.keyCode == 13 || 
		event.keyCode == 18 || event.keyCode == 8 || event.keyCode == 46 || 
		event.keyCode == 37 || event.keyCode == 39 || event.keyCode == 38 ||
		event.keyCode == 35 || event.ctrlKey===true)
	{
		return true;
	}
	else if (key < 48 || key > 57)
	{
    	return false;
	}
	else
	{
		return true;
	};
}