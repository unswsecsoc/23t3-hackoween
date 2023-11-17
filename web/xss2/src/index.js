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
        "470b9baec40b8172557d796badb4aa1836791fc2005df99582d06075336054e4",
      url: req.body.url,
    }),
  });

  res.json({ msg: "Successfully submitted report" });
});

app.use(express.static("static"));

app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});
