$(function () {
  vegaEmbed("#symbol_map", "./charts/map4.vg.json", { actions: false })
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
  vegaEmbed("#reasons_for_visiting", "./charts/reasons_for_visiting.vg.json", {
    actions: false,
  })
    .then(function (result) {
      // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
    })
    .catch(console.error);
});

$(function () {
  vegaEmbed("#monthly_visits", "./charts/monthly_visits.vg.json", {
    actions: false,
  })
    .then(function (result) {
      // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
    })
    .catch(console.error);
});

$(function () {
  vegaEmbed("#spend", "./charts/spend.vg.json", { actions: false })
    .then(function (result) {
      // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
    })
    .catch(console.error);

  vega.expressionFunction("milFormat", function (datum, params) {
    let n = datum / 1000000;
    return n.toString() + "M";
  });

  vega.expressionFunction("moneyFormat", function (datum, params) {
    let n = datum / 1000000000;
    return "$" + n.toString() + "B";
  });
});
