var submit = document.getElementById("submit");
submit.addEventListener("click", displayDetail);

var row = 1;

function displayDetail() {
  let name = document.getElementById("name").value;
  //console.log(name);
  var std = document.getElementById("class").value;
  var gender = document.getElementById("gender").value;
  var grade = document.getElementById("grade").value;
  //console.log(name);

  if (!name || !std || !gender || !grade) {
    alert("Please fill all the entries.....");
    return;
  }

  var display = document.getElementById("display");

  var newRow = display.insertRow(row);
  var cell1 = newRow.insertCell(0);
  var cell2 = newRow.insertCell(1);
  var cell3 = newRow.insertCell(2);
  var cell4 = newRow.insertCell(3);

  cell1.innerHTML = name;
  cell2.innerHTML = std;
  cell3.innerHTML = gender;
  cell4.innerHTML = grade;

  row++;
}
