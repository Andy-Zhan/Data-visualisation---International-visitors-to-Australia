$(function () {
  vegaEmbed("#symbol_map", "../charts/map4.vg.json")
    .then(function (result) {
      // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
    })
    .catch(console.error);
});

// $(function () {
//   vegaEmbed(
//     "#total_visitors_by_year",
//     "../charts/total_visitors_by_year.vg.json"
//   )
//     .then(function (result) {
//       // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
//     })
//     .catch(console.error);
// });

$(function () {
  vegaEmbed("#reasons_for_visiting", "../charts/reasons_for_visiting.vg.json")
    .then(function (result) {
      // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
    })
    .catch(console.error);
});

$(function () {
  vegaEmbed("#monthly_visits", "../charts/monthly_visits.vg.json")
    .then(function (result) {
      // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
    })
    .catch(console.error);
});
