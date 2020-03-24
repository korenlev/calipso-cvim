const {
  FETCH_SCANS,
  FETCH_SCHEDULED_SCANS,
  FETCH_INSTANCES,
  FETCH_LAST_SCAN,
  FETCH_ALERTS,
  METRIC_1,
  METRIC_2,
  METRIC_3,
  METRIC_4,
} = require('../constants/socketIo');

const intervals = [
  {
    message: FETCH_SCANS,
    interval: 15000,
  },
  {
    message: FETCH_SCHEDULED_SCANS,
    interval: 15000,
  },
  {
    message: FETCH_INSTANCES,
    interval: 15000,
  },
  {
    message: FETCH_LAST_SCAN,
    interval: 15000,
  },
  {
    message: FETCH_ALERTS,
    interval: 5000,
  },
  {
    message: METRIC_1,
    interval: 100,
    func: 'random',
  },
  {
    message: METRIC_2,
    interval: 1000,
    func: 'random',
  },
  {
    message: METRIC_3,
    interval: 200,
    func: 'random',
  },
  {
    message: METRIC_4,
    interval: 600,
    func: 'random',
  },
];

const initSocket = (io) => {
  io.on('connection', (socket) => {

    for (let item of intervals) {
      clearInterval(item.timer);
      item.timer = intervalEmit(socket, item);
    }
  });
}

const intervalEmit = (socket, { message, interval, func }) => {
  socket.emit(message, func === 'random' ? 0 : null);

  return setInterval(() => {
    socket.emit(message, func === 'random' ? Math.floor(Math.random() * Math.floor(50)) : null);
  }, interval);
}

module.exports = {
  initSocket,
};
