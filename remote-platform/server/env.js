'use strict';

var server = {
  host: 'localhost',
  port: '9001',
  trust: ['loopback', '192.168.0.0/24']
};


var env = {
  server: server
};


module.exports = env;
