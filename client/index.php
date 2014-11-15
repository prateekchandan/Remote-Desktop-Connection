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

<img id="ItemPreview" src="" />
   

   <canvas id="myCanvas" width="100%" height="100%"></canvas>



<script>
var serverAddr = "ws://<?php echo $_SERVER['SERVER_ADDR']?>:7861"
</script>
<script src="http://code.jquery.com/jquery-2.1.0.min.js"></script>
<script src="js/index.js"></script>
</div>
</body>
</html>
