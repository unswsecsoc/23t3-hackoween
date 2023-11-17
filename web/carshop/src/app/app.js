const express = require("express");
const app = express();
const port = 3000;

const fs = require("fs");

const Handlebars = require("handlebars");

const DYNAMIC_DATA = {
  year: 2023,
  siteName: "Car shop",
};

const render = (res, templateFile, data) => {
  res.send(
    Handlebars.compile(fs.readFileSync(templateFile, { encoding: "utf-8" }))(
      data
    )
  );
};

app.use("/assets", express.static("assets"));

app.get("/", (req, res) => {
  const { p } = req.query;

  if (p) {
    render(res, `views/${p}`, DYNAMIC_DATA);
  } else {
    res.redirect("/?p=index.hbs");
  }
});

app.listen(port, () => {
  console.log(`app listening on port ${port}`);
});
