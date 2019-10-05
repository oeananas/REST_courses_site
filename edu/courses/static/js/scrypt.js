$(document).ready(function () {
  $('[data-toggle="tooltip"]').tooltip();
});

$(function () {

  $("#typing").typed({
    strings: [
      "print('Hello, world!')",
      "func = lambda a, b: a * b",
      "def get_data(self):<br/>&nbsp;&nbsp;&nbsp;&nbsp;return self.data",
      "class Product:<br/>&nbsp;&nbsp;&nbsp;&nbsp;pass",
      "def __init__(self, name):<br/>&nbsp;&nbsp;&nbsp;&nbsp;self.name = name",
      "for i in range(10):<br/>&nbsp;&nbsp;&nbsp;&nbsp;print(i ** 2)",
    ],
    typeSpeed: 5,
    backDelay: 1500,
    startDelay: 2500,
    loop: true,
    loopCount: 1000,
    contentType: 'html',
  });

});

function CountDownTimer(dt, id) {
  let end = new Date(dt);

  let _second = 1000;
  let _minute = _second * 60;
  let _hour = _minute * 60;
  let _day = _hour * 24;
  let timer;

  function showRemaining() {
    let now = new Date();
    let distance = end - now;
    if (distance < 0) {

      clearInterval(timer);
      document.getElementById(id).innerHTML = 'EXPIRED!';

      return;
    }
    let days = Math.floor(distance / _day);
    let hours = Math.floor((distance % _day) / _hour);
    let minutes = Math.floor((distance % _hour) / _minute);
    let seconds = Math.floor((distance % _minute) / _second);

    document.getElementById(id).innerHTML = days + ' DAYS - ';
    document.getElementById(id).innerHTML += hours + ' HOURS - ';
    document.getElementById(id).innerHTML += minutes + ' MIN - ';
    document.getElementById(id).innerHTML += seconds + ' SEC';
  }

  timer = setInterval(showRemaining, 1000);
}
