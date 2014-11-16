<!DOCTYPE HTML>
<html>
<head>

<style type="text/css">
  body {
    overflow:hidden;
  }
  #message{
    max-height: 200px;
  }
  #close-btn{
    position: fixed;
    right: 0px;
    top: 0px;
    color: #FFF;
    background-color: #D9534F;
    border-color: #D43F3A;
    font-size: 14px;
    font-weight: 400;
    line-height: 1.42857;
    text-align: center;
    white-space: nowrap;
    vertical-align: middle;
    cursor: pointer;
  }
  #msg{
    padding: 50px;
    font-color:#666; 
    display: none;
  }
  #connection{
    display: block;
  }
  #ItemPreview{
    margin-left:-9px;
    margin-top:-9px;
    display: none;
  }
</style>
</head>
<body>
<div id="sse">
<button id="close-btn" onclick="disconnect()">Close Connection</button>
<img width="100%" id="ItemPreview" src="" />
<div id="connection">
    <input id="passwd" placeholder="Input Server Password to connect (Max 3 tries)">
    <button onclick="tryconnect()">Connect</button>
    <div id="errmsg"></div>
</div>
<div id="msg">
  <h2>Connection Closed to Server</h2>
  <a href="">Refresh</a> to check connection
</div>
<script>
var serverAddr = "ws://<?php echo $_SERVER['SERVER_ADDR']?>:7861"
</script>
<script src="http://code.jquery.com/jquery-2.1.0.min.js"></script>
<script src="js/index.js"></script>
</div>
</body>
</html>
