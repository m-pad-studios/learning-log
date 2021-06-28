
        var context_2 = document.getElementById('myChart').getContext('2d');
        
        var key_2 = "topic";
        var graph_2 = [topics[key]];
        var count_2 = 0;
        var count_array_2 = [];
        console.log(topics);

        for(var i = 0; i < graph_2.length; i++)
        {
            graph_2[i] = topics[key_2];

        }

        for(var i = 0; i < graph_2[0].length; i++) {
            count_2 += 1;
            console.log(count_2);
            count_array_2[i] = count_2;
        }


     
        var key = "workout";
        var current_user = "logged_user";
        var context = document.getElementById('myChart').getContext('2d');

        var graph = [myData[key]];
        var count = 0;
        var count_array = [];

        for(var i = 0; i < graph.length; i++)
        {
            graph[i] = myData[key];

        }

        for(var i = 0; i < graph[0].length; i++) {
            count += 1;
            console.log(count);
            count_array[i] = count;
        }


        var myChart = new Chart(context, {
            type: 'bar',
            data: {
                labels: ["All workouts", "All topics"],
                datasets: [{
                    label: '# of Workouts & Topics from all users',
                    data: [count,count_2],
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