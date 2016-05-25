<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
  <head>
    <title></title>
  </head>
  <body>
  <form>
    <input id="textMessage" type="text">
    <input onclick="sendMessage();" value="Send Message" type="button">
    <br>
  </form>
  <textarea id="messageTextArea" rows="10" cols="50"></textarea>
  <script type="text/javascript">
    var websocket=new WebSocket("ws://localhost:8080/serverendpointdemo")
    var messageTextArea=document.getElementById("messageTextArea")
    websocket.onopen=function(message) {
      messageTextArea.value+="Connected to server..\n";
    }
    websocket.onclose=function(message) {
      messageTextArea.value+="server closed.\n";
    }
    websocket.onerror=function(message) {
      messageTextArea.value+=("server error."+message+"\n");
    }
    websocket.onmessage=function(message) {
        messageTextArea.value+=("\n"+message.data+"\n");
    }
    function sendMessage() {
      websocket.send(textMessage.value)
      messageTextArea.value+=("sent to server:"+textMessage.value);
      textMessage.value="";
    }
  </script>

  </body>
</html>
