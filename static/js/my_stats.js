
  
        var key_2 = "my_stats";
        var graph_3 = [my_info[key_2]];
        var count_2 = 0;
        var count_array_2 = [];

        console.log("My stats START: ");
        console.log(graph_3);
        console.log(graph_3[0][1].length);

        topic_data = graph_3[0][0];

        console.log(topic_data);

        workout_data = graph_3[0][1];

        console.log(workout_data);



        var myChart = new Chart(context, {
            type: 'pie',
            data: {
                labels: ["All " + userName + "'s' workouts", "All "  + userName + "'s  topics"],
                datasets: [{
                    label: '# of Workouts & Topics from',
                    data: [workout_data.length,topic_data.length],
                    backgroundColor: [
                        'rgba(34, 139, 34, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(34, 139, 34, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
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