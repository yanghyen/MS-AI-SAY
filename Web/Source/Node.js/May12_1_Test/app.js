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

app.listen(5643); // Node.js Express WAS 포트 번호

// http://IP주소:5643/te.st
// app.get("요청주소", function(요청, 응답){});
app.get("/te.st", function(req, ress){
  ress.send("<html><body><marquee>hi</marqee></body></html>");
});

// http://IP주소:5643/param.test?a=10&b=20
app.get("/param.test", function (req, res){
  var aa = req.query.a * 1; // req.query.파라메터변수명
  var bb  =req.query.b * 1; // 글자 -> 숫자 : * 1
  var cc = aa + bb;
  res.send(cc + "");   // 숫자 -> 글자 : + ""
});

// http://IP주소:5643/json.res.test?a=10&b=20
app.get("/json.res.test", function (req, res){
  var aa = req.query.a * 1; 
  var bb  =req.query.b * 1; 
  var cc = aa + bb;
  var dd = {"result" : cc};
  res.setHeader("Access-Control-Allow-Origin", "*")
  res.send(dd);   
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
