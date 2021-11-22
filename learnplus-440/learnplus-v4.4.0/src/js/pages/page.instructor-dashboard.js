(function(){
  'use strict';

  window['moment-range'].extendMoment(moment);

  var earnings = []

  // Create a date range for the last 7 days
  var start = moment().subtract(7, 'days').format('YYYY-MM-DD') // 7 days ago
  var end = moment().format('YYYY-MM-DD') // today
  var range = moment.range(start, end)

  // Create the earnings graph data
  // Iterate the date range and assign a random ($) earnings value for each day
  for (let moment of range.by('days')) {
    earnings.push({
      y: Math.floor(Math.random() * 300) + 10,
      x: moment.toDate()
    })
  }

  var Earnings = function(id, type = 'roundedBar', options = {}) {
    options = Chart.helpers.merge({
      barRoundness: 1.2,
      scales: {
        yAxes: [{
          ticks: {
            maxTicksLimit: 4
          }
        }],
        xAxes: [{
          offset: true,
          ticks: {
            padding: 10
          },
          maxBarThickness: 20,
          gridLines: {
            display: false
          },
          type: 'time',
          time: {
            unit: 'day',
            displayFormats: {
              day: 'D/MM'
            },
            maxTicksLimit: 7
          }
        }]
      }
    }, options)

    var data = {
      datasets: [{
        label: "Earnings",
        data: earnings,
        barThickness: 20
      }]
    }

    Charts.create(id, type, options, data)
  }

  // Create Chart
  Earnings('#earningsChart')

})()