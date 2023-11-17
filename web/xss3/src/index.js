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
        "059aa2841397d9954ed99b3b065dc810c06c7e71d33e1acd8425464e0d31ae76",
      url: req.body.url,
    }),
  });

  res.json({ msg: "Successfully submitted report" });
});

app.use(express.static("static"));

app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});
