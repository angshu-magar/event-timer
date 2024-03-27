let eventTimeDiv = document.getElementById("time");
let eventTime = new Date(eventTimeDiv.innerHTML).getTime();
let daysDiv = document.getElementById("days");
let hoursDiv = document.getElementById("hours");
let minutesDiv = document.getElementById("minutes");
let secondsDiv = document.getElementById("seconds");

function update_countdown()
{
    let now = new Date().getTime();
    let difference = eventTime - now;
    if (difference < 0){
        difference = now - eventTime;
    }

    let days = Math.floor(difference / (1000 * 60 * 60 * 24));
    let hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((difference % (1000 * 60)) / 1000);
    daysDiv.innerHTML = days;
    hoursDiv.innerHTML = hours;
    minutesDiv.innerHTML = minutes;
    secondsDiv.innerHTML = seconds;
}
update_countdown();
setInterval(update_countdown, 1000);
