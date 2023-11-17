async function reportPage() {
  const urlRaw = document.getElementById("url").value;

  let submitUrl;

  try {
    submitUrl = new URL(urlRaw);
  } catch {
    alert("Please enter a url starting with " + location.origin);
    return;
  }

  if (submitUrl.origin !== location.origin) {
    alert("Please enter a url starting with " + location.origin);
    return;
  }

  const submitData = urlRaw.substring(location.origin.length + 1);

  fetch("/api/report", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      url: submitData,
    }),
  })
    .then((resp) => resp.json())
    .then((data) => alert(data.msg))
    .catch((err) => alert("An error occurred! " + err.toString()));
}
