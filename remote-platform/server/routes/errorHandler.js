var express = require('express');
var router = express.Router();

router.use(function(err, req, res, next) {
  console.error(err.stack)
  res.status(500).send('Server error!');
});

module.exports = router;
