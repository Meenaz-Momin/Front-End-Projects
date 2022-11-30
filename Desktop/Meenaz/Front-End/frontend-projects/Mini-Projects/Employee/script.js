let btn = document.getElementById("add");

btn.addEventListener("click", () => {
  const id = document.getElementById("id").value;
  const name = document.getElementById("name").value;
  const salary = document.getElementById("salary").value;
  const city = document.getElementById("city").value;
  let table = document.querySelector(".table");

  if (!id || !name || !salary || !city) {
    alert("Please fill all the fields");
    return;
  }

  let newRow = table.insertRow(table.length);
  let c1 = newRow.insertCell(0);
  let c2 = newRow.insertCell(1);
  let c3 = newRow.insertCell(2);
  let c4 = newRow.insertCell(3);
  let c5 = newRow.insertCell(4);

  c1.innerHTML = id;
  c2.innerHTML = name;
  c3.innerHTML = salary;
  c4.innerHTML = city;
  c5.innerHTML = `<a onclick=onEdit(this) href="#" >Edit</a>
                  <a onclick=onDelete(this) href="#" >Delete</a>`;
  reset();
});

function reset() {
  document.getElementById("id").value = "";
  document.getElementById("name").value = "";
  document.getElementById("salary").value = "";
  document.getElementById("city").value = "";
}

function onEdit(td) {
  document.getElementById("id").value =
    td.parentNode.parentNode.cells[0].textContent;
  document.getElementById("name").value =
    td.parentNode.parentNode.cells[1].textContent;
  document.getElementById("salary").value =
    td.parentNode.parentNode.cells[2].textContent;
  document.getElementById("city").value =
    td.parentNode.parentNode.cells[3].textContent;
  td.parentElement.parentElement.remove();
}
function onDelete(td) {
  td.parentElement.parentElement.remove();
}
