const nameInput = document.getElementById("name");
const result = document.getElementById("result");

function setName(newName) {
  result.innerHTML = "Welcome, " + newName + "! How are you going?";
}

function buttonpress() {
  location.hash = nameInput.value;

  setName(nameInput.value);
}

if (location.hash.length > 1) {
  setName(decodeURI(location.hash.substring(1)));
}
