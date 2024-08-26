function startCountdown() {
  let timer = setInterval(function() {
    let minutes = Math.floor(countdownTime / 60);
    let seconds = countdownTime % 60;

    minutes = minutes < 10 ? '0' + minutes : minutes;
    seconds = seconds < 10 ? '0' + seconds : seconds;

    document.getElementById('countdown_timer').innerHTML = minutes + ':' + seconds;

    if (countdownTime <= 0) {
        clearInterval(timer);
        alert('Time is up!');
    }

    countdownTime--;
  }, 1000);
}

window.onload = startCountdown;