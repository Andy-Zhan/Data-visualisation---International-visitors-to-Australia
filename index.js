$(function () {
  var spec2 = "map3.vg.json";
  vegaEmbed("#symbol_map", spec2)
    .then(function (result) {
      // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
    })
    .catch(console.error);
});
