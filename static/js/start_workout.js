"use strict";

// IIFE for faster load time.
(function () {
  window.onload = function () {
    let seconds = 00;
    let tens = 00;
    let appendTens = document.getElementById("tens");
    let appendSeconds = document.getElementById("seconds");
    let buttonStart = document.getElementById("button-start");
    let buttonStop = document.getElementById("button-stop");
    let buttonReset = document.getElementById("button-reset");
    let Interval;

    buttonStop.hidden = true;

    buttonStart.onclick = function () {
      buttonStart.hidden = true;
      buttonStart.disabled = true;

      buttonStop.hidden = false;
      buttonStop.disabled = false;
      clearInterval(Interval);
      Interval = setInterval(startTimer, 10);
    };

    buttonStop.onclick = function () {
      buttonStop.hidden = true;
      buttonStop.disabled = true;

      buttonStart.hidden = false;
      buttonStart.disabled = false;

      clearInterval(Interval);
    };

    buttonReset.onclick = function () {
      clearInterval(Interval);
      tens = "00";
      seconds = "00";
      appendTens.innerHTML = tens;
      appendSeconds.innerHTML = seconds;
    };

    function startTimer() {
      tens++;

      if (tens <= 9) {
        appendTens.innerHTML = "0" + tens;
      }

      if (tens > 9) {
        appendTens.innerHTML = tens;
      }

      if (tens > 99) {
        console.log("seconds");
        seconds++;
        appendSeconds.innerHTML = "0" + seconds;
        tens = 0;
        appendTens.innerHTML = "0" + 0;
      }

      if (seconds > 9) {
        appendSeconds.innerHTML = seconds;
      }
    }
  };
})();
