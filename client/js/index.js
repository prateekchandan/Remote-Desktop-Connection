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

var mouseEvents = [];
var keyEvents = new Array();

$(document).keydown(function (e) {
	e.preventDefault();
	keyEvents.push(e.which);
	console.log(keyEvents);
});

$(document).keyup(function (e) {
	e.preventDefault();
	keyEvents.push(-e.which);
	console.log(keyEvents);
});

$(document).scroll(function(e) {
if (e.originalEvent.wheelDelta >= 0) {
        console.log('Scroll up');
    }
    else {
        console.log('Scroll down');
    }
});

$('#ItemPreview').mousedown(function(e) {
	var x = e.pageX - e.target.offsetLeft;
	var y = e.pageY - e.target.offsetTop;
	console.log(x, y);
});

function changeimage(){
	var str = ''
		ws.send(str);
}
setInterval(changeimage, 50);

function disconnect(){
	ws.send("exit");
}
