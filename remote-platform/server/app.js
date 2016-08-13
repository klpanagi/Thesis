'use strict';

var path = require('path');
var express = require('express');
var logger = require('morgan');  // Use logger
var bodyParser = require('body-parser');
var cookieParser = require('cookie-parser');

var routespath = path.join(__dirname, 'routes');

/**
 * Import routers.
 */
var index = require(path.join(routespath, 'index.js'));
var errorHandler = require(path.join(routespath, 'errorHandler.js'));

var app = express();


/**
 * Setup view engine
 */
app.set('views', './views');
app.set('view engine', 'pug');
app.locals.pretty = true;  // indent produces HTML for clarity


/**
 * Middleware
 */
app.use(logger('combined', { }));
app.use(bodyParser.json());  // Parse application/json
app.use(bodyParser.urlencoded({ extended: true }));  // Parse application/x-www-urlencoded
app.use(cookieParser());


/**
 * Static files
 */
app.use('/static/bootstrap',
  express.static(path.join(__dirname, 'node_modules/bootstrap')));
app.use('/static/jquery',
  express.static(path.join(__dirname, 'node_modules/jquery')));
app.use('/static/public',
  express.static(path.join(__dirname, 'public')));


/**
 * Add routers to the application.
 */
app.use(index);
app.use(errorHandler);


module.exports = app;
