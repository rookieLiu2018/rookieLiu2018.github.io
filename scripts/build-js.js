const fs = require("fs");
const UglifyJS = require("uglify-js");

const sourcePaths = [
  "node_modules/jquery/dist/jquery.min.js",
  "assets/js/plugins/jquery.greedy-navigation.js",
  "assets/js/_main.js",
];
const themeSource = fs.readFileSync("assets/js/theme.js", "utf8");
const lightThemeMarker = "// light theme";
const lightThemeStart = themeSource.indexOf(lightThemeMarker);

if (lightThemeStart === -1) {
  throw new Error("Could not find the Plotly light theme in assets/js/theme.js");
}

const sources = sourcePaths.map((path) => fs.readFileSync(path, "utf8"));
sources.push(themeSource.slice(lightThemeStart));

const result = UglifyJS.minify(sources, {
  compress: true,
  mangle: true,
  module: true,
});

if (result.error) {
  throw result.error;
}

fs.writeFileSync("assets/js/main.min.js", result.code);
