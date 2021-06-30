
        var context_2 = document.getElementById('myChart').getContext('2d');
        
        var key_2 = "topics";
        var graph_2 = [topics[key]];
        var count_2 = 0;
        var count_array_2 = [];
        //console.log(topics);

        for(var i = 0; i < graph_2.length; i++)
        {
            graph_2[i] = topics[key_2];
            count_2 += 1;
        }


     
        var key = "workouts";
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
          //  console.log(count);
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
                        'rgba(34, 139, 34, 0.5)',
                        'rgba(54, 162, 235, 0.5)',
               
                    ],
                    borderColor: [
                        'rgb(0, 0, 0)',
                        'rgb(0, 0, 0)',
                        'rgb(0, 0, 0)',
                        'rgb(0, 0, 0)',
                        'rgb(0, 0, 0)',
                        'rgb(0, 0, 0)'
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