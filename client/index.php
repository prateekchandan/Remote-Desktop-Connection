<!DOCTYPE HTML>
<html>
<head>

<style type="text/css">
  #message{
    max-height: 200px;
  }
</style>
</head>
<body>
<div id="sse">
   <div id="message">
   </div>
   <button onclick="disconnect()">DISCONNECT</button>
  <br>
  <br>
  <br>
  <br>
   

   <canvas id="myCanvas" width="1300" height="768"></canvas>
   <script type="text/javascript">


var ws=0

  if ("WebSocket" in window)
  {
      document.getElementById('message').innerHTML="WEB SOCKET SUPPORTED";
     // Let us open a web socket
     ws = new WebSocket("ws://<?php echo $_SERVER['SERVER_ADDR']?>:7861");
     ws.onopen = function()
     {
        // Web Socket is connected, send data using send()
        document.getElementById('message').innerHTML+="<br>Connected";
     };
     ws.onmessage = function (evt) 
     { 
        var received_msg = evt.data;
        var d = new Date();
        console.log("Recieve: "+d.getTime());
        received_msg=JSON.parse(received_msg);
        fillRect(received_msg)
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
  

//while(1)
//  ws.send("hello");
</script>


<script>


function fillRect(myarray){
  var c = document.getElementById("myCanvas");
  var ctx = c.getContext("2d");
  for (var i = 0; i < myarray.length; i++) {
    data=myarray[i];
    ctx.fillStyle = "#"+data[2];    
    ctx.fillRect( data[0]-1, data[1]-1, data[0], data[1] );
  };
}

var r=0,g=0,b=0;
function changeimage(){
  var str=r+","+g+","+b
  var d = new Date();
  console.log("Sent: "+d.getTime());
  ws.send(str);
  r=(r+1)%255;
  if(r==0)
    g+=100
}
setInterval(changeimage, 1000);

function disconnect(){
  ws.send("exit");
}
</script>
</div>
</body>
</html>