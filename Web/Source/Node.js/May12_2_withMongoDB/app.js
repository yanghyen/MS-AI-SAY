var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.listen(7899);

// http://IP:7899/snack.reg?name=XXX&price=YYY
app.get("/snack.reg", function(rq,rs){
  var mjs = require("mongojs");
  // var db = mjs("서버주소/DB명", ["테이블명", "테이블명",...])
  var db = mjs("195.168.9.126/yanghyenTS", ["may12_snack"]);
  var n = rq.query.name;
  var p = rq.query.price;

  db.may12_snack.insertOne({name: n, price: p}, function(err,result){
    rs.setHeader("Access-Control-Allow-Origin", "*");
    rs.send(result);
  });
});

// http://IP:7899/snack.get?name=XXX&price=YYY
app.get("/snack.get", function(rq,rs){
  var db = require("mongojs")("195.168.9.126/yanghyenTS", ["may12_snack"]);

  db.may12_snack.find(function(err,result){
    rs.setHeader("Access-Control-Allow-Origin", "*");
    rs.send(result);
  });
});

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
