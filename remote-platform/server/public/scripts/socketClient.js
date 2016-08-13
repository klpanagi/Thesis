var io = require('socket.io-client');

var socket = io();

socket.on('connect', function (client) {
  console.log('Client connected to the socket.io server');
});


module.exports = socket;
