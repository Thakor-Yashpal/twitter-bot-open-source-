function updateClock() {
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();
    var clock = document.getElementById("clock");
    clock.innerHTML = hours + ":" + minutes + ":" + seconds;
  }
  setInterval(updateClock, 1000);

  var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  var day = days[now.getDay()];
  var date = now.getDate();
  var month = months[now.getMonth()];
  var year = now.getFullYear();
  clock.innerHTML = day + ", " + date + " " + month + " " + year + " " + hours + ":" + minutes + ":" + seconds;
