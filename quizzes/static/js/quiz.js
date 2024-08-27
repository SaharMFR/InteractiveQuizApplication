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
        document.getElementById('quiz').submit();
    }

    countdownTime--;
  }, 1000);
}

window.onload = startCountdown;

// function startCountdown() {
//   // Set the total countdown time in seconds (e.g., 5 minutes = 300 seconds)
//   let totalTime = 300; // Adjust this value as needed
//
//   // Get the start time from localStorage, or set it to the current time
//   let startTime = localStorage.getItem('quizStartTime') || new Date().getTime();
//   localStorage.setItem('quizStartTime', startTime);
//
//   // Calculate the elapsed time
//   let elapsedTime = Math.floor((new Date().getTime() - startTime) / 1000);
//   let countdownTime = totalTime - elapsedTime;
//
//   // If time is up, submit the form immediately
//   if (countdownTime <= 0) {
//     alert('Time is up!');
//     document.getElementById('quiz').submit();
//     return;
//   }
//
//   let timer = setInterval(function () {
//     let minutes = Math.floor(countdownTime / 60);
//     let seconds = countdownTime % 60;
//
//     minutes = minutes < 10 ? '0' + minutes : minutes;
//     seconds = seconds < 10 ? '0' + seconds : seconds;
//
//     document.getElementById('countdown_timer').innerHTML = minutes + ':' + seconds;
//
//     if (countdownTime <= 0) {
//       clearInterval(timer);
//       alert('Time is up!');
//       document.getElementById('quiz').submit();
//     }
//
//     countdownTime--;
//   }, 1000);
// }
//
// window.onload = startCountdown;