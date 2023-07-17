// calling /piedata route in app.py
const url = "piedata";

fetch(url)
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
    // create empty array and total counter
    states_list = [];
    total_count = 0;
    other_counter = 0;

    //total counted
    for (i=0; i<27; i++) {
      counter = data[i].count;
      total_count = total_count + counter;
    };

    //put data in array
    for (i=0; i<data.length; i++) {
      sname = data[i]._id.province;
      sytry = (data[i].count/total_count) *100;
      let sy = Math.floor(sytry*100)/100;
      //if percentage = 0 then continue to next i++
      if (Math.floor(sy) == 0) {
        other_counter = other_counter + sy;
        continue;
      }
      //if no length then add first element with needed info
      if (states_list.length == 0) {
        states_list.push({
        name: sname,
        y: sy,
        sliced: true,
        selected: true,
        });
      }
      //everything else gets logged as normal
      else {
        states_list.push({
          name: sname,
          y: sy,
        });
      }
    };

    //push others that were equal to a rounded 0 onto list
    states_list.push({
      name: "Others",
      y: other_counter,
    });

    //see the list that was filtered and created
    console.log(states_list);

    Highcharts.chart("container", {
      chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: "pie",
      },
      title: {
          text: 'Most Logged Provinces/States (U.S. Only)',
          align: 'left'
      },
      tooltip: {
        pointFormat: "{series.name}: <b>{point.percentage:.1f}%</b>",
      },
      accessibility: {
        point: {
          valueSuffix: "%",
        },
      },
      plotOptions: {
        pie: {
          allowPointSelect: true,
          cursor: "pointer",
          dataLabels: {
            enabled: true,
            format: "<b>{point.name}</b>: {point.percentage:.1f} %",
          },
        },
      },
      series: [
        {
          name: "Amount Logged",
          colorByPoint: true,
          data: states_list,
        },
      ],
    });
  });
