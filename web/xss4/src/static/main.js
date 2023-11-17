const descInput = document.getElementById("desc");
const nameInput = document.getElementById("name");
const result = document.getElementById("result");

function setDescription(newDesc) {
  result.innerHTML = DOMPurify.sanitize("Description: " + newDesc);
}

function setName(newName) {
  if (newName.length >= 24) {
    alert("BAD INPUT");
    return;
  }

  result.innerHTML += "<br>Welcome, " + newName + "! How are you going?";
}

function buttonpress() {
  location.hash = descInput.value + "&" + nameInput.value;

  setDescription(descInput.value);
  setName(nameInput.value);
}

if (location.hash.length > 1) {
  parts = decodeURI(location.hash.substring(1)).split("&");
  setDescription(parts[0]);
  setName(parts[1]);
}
