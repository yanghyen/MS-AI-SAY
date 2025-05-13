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

// var si = require("socket.io");
// var io = si(); 를 한줄로 처리
var io = require("socket.io")();
io.listen(9999);  // socket 통신 포트 번호

// app.listen(port번호); 는 Node.js를 HTTP 통신할 때 씀

// 웹소켓서비스 시작 -> 이걸 자동으로 만들어줌
// http://주소:포트/socket.io/socket.io.js

io.sockets.on("connection", function(socket){
  console.log("채팅 연결");
  socket.on("hi", function(h){
    socket.emit("bye", h);
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
