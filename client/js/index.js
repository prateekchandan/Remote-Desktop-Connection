var ws=0

if ("WebSocket" in window)
{
	document.getElementById('message').innerHTML="WEB SOCKET SUPPORTED";
	// Let us open a web socket
	ws = new WebSocket(serverAddr);
	ws.onopen = function()
	{
		// Web Socket is connected, send data using send()
		document.getElementById('message').innerHTML+="<br>Connected";
	};
	ws.onmessage = function (evt) 
	{ 
		var received_msg = evt.data;
		var d = new Date();
		fillRect(received_msg);
	};
	ws.onclose = function()
	{ 
		// websocket is closed.
		document.getElementById('message').innerHTML+="<br>Connection closed By Server";
	}
}
else
{
	// The browser doesn't support WebSocket
	document.getElementById('message').innerHTML="WEB SOCKET CONNECTION FAILED";
}


function fillRect(myarray){
	document.getElementById("ItemPreview").src = "data:image/png;base64," + myarray;
}


/**
 * mouseEvents and keyEvents capture
 */

$('#ItemPreview').height($(window).height());

var mouseEvents = new Array();
var keyEvents = new Array();
var curKeys = [];
for(var i = 0; i < 1000; i++) {
	curKeys.push(false);
}

$(document).keydown(function (e) {
	if(e.which != 122 && e.which != 123) e.preventDefault();
	if(!curKeys[e.which]){ 
		keyEvents.push(e.which);
	}
	curKeys[e.which] = true;
});

$(document).keyup(function (e) {
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
	var message = keyEvents.join().concat('|').concat(mouseEvents.join()).concat('|').concat(getMouseCoord());
	keyEvents = new Array();
	mouseEvents = new Array();
	console.log(message);
	ws.send(message);
}
setInterval(changeimage, 50);

function disconnect(){
	ws.send("exit");
}
