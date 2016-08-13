'use strict';

var express = require('express');
var router = express.Router();


router.get('/', function(req, res) {
  res.render('home', {
    //debug: true,
    title: 'Welcome',
    user: '',
    connectionInfo: {
      'Remote host': req.connection.remoteAddress,
      'Remote port': req.connection.remotePort
    }
  });
});


module.exports = router;
