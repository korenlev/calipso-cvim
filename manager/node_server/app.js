// this is a comment  
const express = require('express');
const path = require('path');
const logger = require('morgan');

const grafanaRouter = require('./routes/grafana');
const inventoryRouter = require('./routes/inventory');
const prometheusRouter = require('./routes/prometheus');
const scansRouter = require('./routes/scans');
const scheduleScansRouter = require('./routes/scheduleScan');
const timezoneRouter = require('./routes/timezone')

const app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', grafanaRouter);
app.use('/inventory', inventoryRouter);
app.use('/prometheus', prometheusRouter);
app.use('/scans', scansRouter);
app.use('/latest_scans', scansRouter);
app.use('/scheduled_scans', scheduleScansRouter);
app.use('/timezone', timezoneRouter);

// error handler
app.use((err, req, res, next) => {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
