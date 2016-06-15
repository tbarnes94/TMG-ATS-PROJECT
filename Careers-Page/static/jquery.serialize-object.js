function sendForm(){
model_data = $("#frm").serializeObject();
$.ajax({
url: 'YOUR_SERVICE_URL',
type: 'POST',
contentType: 'application/json',
data: JSON.stringify(model_data),
dataType: 'json',
success:function(e){
    // I know, you do not want Ajax, if you callback to page, you can refresh page here
    }
});
