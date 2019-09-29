$(document).ready(function () {
  $('[data-toggle="tooltip"]').tooltip();
});

$(function () {

  $("#typing").typed({
    strings: [
      "print('Hello, world!')",
      "return a * b",
      "def get_data(self):<br/>&emsp;return self.data",
      "class Product:<br/>&emsp;pass",
      "def __init__(self, name):<br/>&emsp;self.name = name",
      "for i in range(10):<br/>&emsp;print(i ** 2)",
    ],
    typeSpeed: 5,
    backDelay: 1500,
    startDelay: 2500,
    loop: true,
    loopCount: 1000,
    contentType: 'html',
  });

});
