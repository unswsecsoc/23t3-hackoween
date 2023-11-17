const nameInput = document.getElementById("name");
const result = document.getElementById("result");

function setName(newName) {
  if (newName.indexOf("onerror") >= 0 || newName.indexOf("onload") >= 0) {
    alert("BAD INPUT");
    return;
  }

  result.innerHTML = "Welcome, " + newName + "! How are you going?";
}

function buttonpress() {
  location.hash = nameInput.value;

  setName(nameInput.value);
}

if (location.hash.length > 1) {
  setName(decodeURI(location.hash.substring(1)));
}
