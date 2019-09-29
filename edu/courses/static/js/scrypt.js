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
