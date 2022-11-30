let screen = document.getElementById("screen");
buttons = document.querySelectorAll("button");
let screenvalue = "";
for (item of buttons) {
  item.addEventListener("click", (e) => {
    buttonText = e.target.innerText;
    console.log("text button is", buttonText);
    if (buttonText == "=") {
      screen.value = eval(screenvalue);
    } else if (buttonText == "C") {
      screenvalue = "";
      screen.value = screenvalue;
    } else {
      screenvalue += buttonText;
      screen.value = screenvalue;
    }
  });
}
