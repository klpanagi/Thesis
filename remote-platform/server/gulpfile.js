'use strict';

var gulp = require('gulp');
var browserify = require('gulp-browserify');
var rename = require('gulp-rename');
var clean = require('gulp-clean');


/**
 * Gulp Tasks
 */
gulp.task('bundle', function() {
  gulp.src('./public/scripts/client.js')
      .pipe(browserify({
        insertGlobals : true,
        debug : true
      }))
      .pipe(rename('bundle.js'))
      .pipe(gulp.dest('./public/build/'));
});


gulp.task('clean', function () {
  return gulp.src('./public/build', {read: false})
    .pipe(clean());
});
