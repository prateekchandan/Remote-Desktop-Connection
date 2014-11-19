var ws=0
var state=0;

if ("WebSocket" in window)
{
	// Let us open a web socket
	ws = new WebSocket(serverAddr);
	ws.onopen = function()
	{
		// Web Socket is connected, send data using send()
	};
	ws.onmessage = function (evt) 
	{ 
		if(state){
			var received_msg = evt.data;
			ChangeFrame(received_msg);
		}
		else{
			var received_msg = evt.data;
			if(received_msg=="connect")
			{
				state=1
				$('#ItemPreview').css('display','block');	
				$('#connection').css('display','none');	
				$('#msg').css('display','none');		
			}
			else 
			{
				$("#errmsg").html("Error in Password");
			}
		}
	};
	ws.onclose = function()
	{ 
		// websocket is closed.
		$('#ItemPreview').css('display','none');	
		$('#connection').css('display','none');	
		$('#msg').css('display','block');	

	}
}
else
{
	$('#ItemPreview').css('display','none');	
	$('#connection').css('display','none');	
	$('#msg').css('display','block');	
	
}


function ChangeFrame(data){
	var reader = new window.FileReader();
	reader.readAsDataURL(data); 
	reader.onloadend = function() {
				document.getElementById("ItemPreview").src =  reader.result;
  	}
}


/**
 * mouseEvents and keyEvents capture
 */

$(window).resize(function(){
	$('#ItemPreview').height($(window).height());
	$('#ItemPreview').width($(window).width());
})
$('#ItemPreview').height($(window).height());
$('#ItemPreview').width($(window).width());

var mouseEvents = new Array();
var keyEvents = new Array();
var curKeys = [];

for(var i = 0; i < 1000; i++) {
	curKeys.push(false);
}

$(document).keydown(function (e) {
	if(state==0)
		return;
	if(e.which != 122 && e.which != 123) e.preventDefault();
	if(!curKeys[e.which]){ 
		keyEvents.push(e.which);
	}
	curKeys[e.which] = true;
});

$(document).keyup(function (e) {
	if(state==0)
		return;
	e.preventDefault();
	keyEvents.push(-e.which);
	curKeys[e.which] = false;
});


$('#ItemPreview').bind('mousewheel', function(e){
	if(e.originalEvent.wheelDelta /120 > 0) {
		var arr = [parseInt(mouse.x-$('#ItemPreview').offset().left)*1000.0/parseInt($('#ItemPreview').css('width')), parseInt(mouse.y-$('#ItemPreview').offset().top)*1000.0/parseInt($('#ItemPreview').css('height')), 4];
		mouseEvents.push(arr.join(' '));
	}
	else{
		var arr = [parseInt(mouse.x-$('#ItemPreview').offset().left)*1000.0/parseInt($('#ItemPreview').css('width')), parseInt(mouse.y-$('#ItemPreview').offset().top)*1000.0/parseInt($('#ItemPreview').css('height')), 5];
		mouseEvents.push(arr.join(' '));
	}
});

$('#ItemPreview').mousedown(function(e) {
	e.preventDefault();
	var x = parseInt(e.pageX - e.target.offsetLeft)*1000.0/parseInt($(this).css('width'));
	var y = parseInt(e.pageY - e.target.offsetTop)*1000.0/parseInt($(this).css('height'));
	var type = e.which;
	var arr = [x, y, type];
	mouseEvents.push(arr.join(' '));
});

$('#ItemPreview').mouseup(function(e) {
	e.preventDefault();
	var x = parseInt(e.pageX - e.target.offsetLeft)*1000.0/parseInt($(this).css('width'));
	var y = parseInt(e.pageY - e.target.offsetTop)*1000.0/parseInt($(this).css('height'));
	var type = e.which;
	var arr = [x, y, -type];
	mouseEvents.push(arr.join(' '));
});

function getMouseCoord(){
	var a = [parseInt(mouse.x-$('#ItemPreview').offset().left)*1000.0/parseInt($('#ItemPreview').css('width')), parseInt(mouse.y-$('#ItemPreview').offset().top)*1000.0/parseInt($('#ItemPreview').css('height'))];
	console.log($('#ItemPreview').height());
	a = a.join();
	return a;
}

var mouse = {x: 0, y: 0};

document.addEventListener('mousemove', function(e){ 
    mouse.x = e.clientX || e.pageX; 
    mouse.y = e.clientY || e.pageY 
}, false);

function changeimage(){
	if(state==0)
		return;
	var message = keyEvents.join().concat('|').concat(mouseEvents.join()).concat('|').concat(getMouseCoord());
	keyEvents = new Array();
	mouseEvents = new Array();
	//console.log(message);
	ws.send(message);
}
setInterval(changeimage, 300);

function disconnect(){
	ws.send("exit");
	ws.close();
	$('#ItemPreview').css('display','none');	
	$('#msg').css('display','block');	
	$('#connection').css('display','none');	

	state=0;
}


function tryconnect () {
	var passwd=$("#passwd").val();
	ws.send(passwd);
}
