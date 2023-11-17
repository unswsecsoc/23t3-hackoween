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
        "8ea4dc1b6e3bb5a9d710b01ee337bafcd26d433ef8fd3c8b73c151bf0cf89b9d",
      url: req.body.url,
    }),
  });

  res.json({ msg: "Successfully submitted report" });
});

app.use(express.static("static"));

app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});
