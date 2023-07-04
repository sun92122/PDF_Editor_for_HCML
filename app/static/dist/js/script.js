/*!
* Start Bootstrap - Bare v5.0.9 (https://startbootstrap.com/template/bare)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-bare/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

var form = document.querySelector('.main-form');
form.addEventListener('change', function (e) {
  // update the value to python script
  var data = new FormData(form);
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/', true);
  xhr.onload = function () {
    // do something to response
    console.log(this.responseText);
  }
  xhr.send(data);
  // reload the page
  location.reload();
}, false)
