const secHand = document.querySelector(".sec");
const minHand = document.querySelector(".min");
const hrsHand = document.querySelector(".hrs");
let box = document.querySelector(".box");

function setTime() {
  let now = new Date();
  let sec = now.getSeconds();
  let min = now.getMinutes();
  let hrs = now.getHours();

  const secDeg = (sec / 60) * 360 + 90;
  secHand.style.transform = `rotate(${secDeg}deg)`;

  const minDeg = (min / 60) * 360 + 90;
  minHand.style.transform = `rotate(${minDeg}deg)`;

  const hrsDeg = (hrs / 60) * 360 + 90;
  hrsHand.style.transform = `rotate(${hrsDeg}deg)`;
}

setInterval(setTime, 1000);

setTime();
function displayTime() {
  let d = new Date();
  let h = d.getHours();
  let m = d.getMinutes();
  let s = d.getSeconds();
  let time = h + ":" + m + ":" + s;
  if (a === 1) {
    const name = document.createTextNode(time);
    box.appendChild(name);
    var a = 0;
  } else {
    box.textContent = time;
  }
}
setInterval(displayTime, 1000);
displayTime();
