
  "use strict";


  (function() {
    var key_2 = "my_stats";
    var graph_3 = [my_info[key_2]];

    var count_2 = 0;
    var count_array_2 = [];

  
    var topic_data = graph_3[0][0];



    var workout_data = graph_3[0][1];





    var myChart = new Chart(context, {
        type: 'pie',
        data: {
            labels: ["All " + userName + "'s' workouts", "All "  + userName + "'s  topics"],
            datasets: [{
                label: '# of Workouts & Topics from',
                data: [workout_data.length,topic_data.length],
                backgroundColor: [
                    'rgba(34, 139, 34, 0.5)',
                    'rgba(54, 162, 235, 0.5)',
                    'rgba(255, 206, 86, 0.5)',
                    'rgba(75, 192, 192, 0.5)',
                    'rgba(153, 102, 255, 0.5)',
                    'rgba(255, 159, 64, 0.5)'
                ],
                borderColor: [
                    'rgb(0, 0, 0)',
                    'rgb(0, 0, 0)',
                    'rgb(0, 0, 0)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

  }());
      