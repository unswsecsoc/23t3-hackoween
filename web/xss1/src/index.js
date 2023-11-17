const express = require("express");
const app = express();
const port = 3000;

const fetch = require("node-fetch");

app.use(express.json());

app.post("/api/report", async (req, res) => {
  await fetch("http://xssbot:1337/visit", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      runHash:
        "a516819e01af75f8cd03334cb3c8780b06e493e4ba45424cd184c33581c8e129",
      url: req.body.url,
    }),
  });

  res.json({ msg: "Successfully submitted report" });
});

app.use(express.static("static"));

app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});
