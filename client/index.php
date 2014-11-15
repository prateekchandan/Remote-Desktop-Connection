<!DOCTYPE HTML>
<html>
<head>

<style type="text/css">
  #message{
    max-height: 200px;
  }
  #close-btn{
    position: fixed;
    right: 0px;
    top: 0px;
  }
  #msg{
    padding: 50px;
    font-color:#666; 
    display: none;
  }
</style>
</head>
<body>
<div id="sse">
<button id="close-btn" onclick="disconnect()">Close Connection</button>
<img width="100%" id="ItemPreview" src="" />
<div id="msg">
</div>
<script>
var serverAddr = "ws://<?php echo $_SERVER['SERVER_ADDR']?>:7861"
</script>
<script src="http://code.jquery.com/jquery-2.1.0.min.js"></script>
<script src="js/index.js"></script>
</div>
</body>
</html>
