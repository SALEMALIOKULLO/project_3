const url= "bardata";

fetch(url)
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
  });
Highcharts.chart('container', {

    chart: {
        type: 'variwide'
    },

    title: {
        text: 'Wine, Country vs Price'
    },

    subtitle: {
        text: 'Source: winemag-data-130k-v2.csv' + 'Salem Okullos research'
    },

    xAxis: {
        type: 'category'
    },

    caption: {
        text: 'Column widths are proportional to Countries wine GDP'
    },

    legend: {
        enabled: false
    },

    series: [{
        name: 'Average Priced: Wine',
        data: [
            ['USA', 35.57, 54504],
            ['France', 41.1, 22093],
            ['Italy', 39.6, 19504],
            ['Portugal', 26.2, 5691],
            ['Chile', 20.78, 4472],
            ['Argintina', 24.51, 3800],
            ['Austria', 30.76, 3345],
            ['Australia', 35.44, 2329],
            ['New Zealand', 26.93, 1419],
            ['South Africa', 24.67, 1401],
            ['Mexico', 26.78, 70],
            ['Canada', 35.71, 257],
            ['Uruguay', 26.4, 109],
            ['India', 13.3, 9],
            ['Switzerland', 85.28, 7],
            ['Germany', 42.25, 2165],
            ['Greece', 22.36, 466],
            ['Isael', 31.77, 505]

        ],
        dataLabels: {
            enabled: true,
            format: '$ {point.y:.0f}'
        },
        tooltip: {
            pointFormat: 'Average Price: <b>$ {point.y}</b><br>' +
                'GDP: <b> {point.z} bottles </b><br>'
        },
        borderRadius: 3,
        colorByPoint: true
    }]

});
