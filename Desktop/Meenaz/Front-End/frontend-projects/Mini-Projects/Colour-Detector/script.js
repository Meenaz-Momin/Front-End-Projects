const red = document.querySelector(".red");
const yellow = document.querySelector(".yellow");
const pink = document.querySelector(".pink");
const brown = document.querySelector(".brown");
const black = document.querySelector(".black");
const white = document.querySelector(".white");
const green = document.querySelector(".green");
const darkGreen = document.querySelector(".darkGreen");
const skyBlue = document.querySelector(".skyBlue");
const orange = document.querySelector(".orange");
const darkBlue = document.querySelector(".darkBlue");

const display = document.querySelector(".display");

let arr = [
  red,
  yellow,
  pink,
  brown,
  black,
  white,
  green,
  darkGreen,
  skyBlue,
  orange,
  darkBlue,
];
for (let i = 0; i < arr.length; i++) {
  arr[i].addEventListener("mouseenter", () => {
    display.style.backgroundColor = window.getComputedStyle(
      arr[i]
    ).backgroundColor;
   /* display.innerHTML = arr[i];*/
  });
  /*arr[i].addEventListener("onmouseout",() => {
    display.style.backgroundColor = "";
  })*/
}

/* console.log(window.getComputedStyle(arr[i]).backgroundColor);*/
