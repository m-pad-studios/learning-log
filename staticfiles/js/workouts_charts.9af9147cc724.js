 var myData= {{ serialized_data | safe }};
        var key = "workout";
        var current_user = "logged_user";

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

        console.log("The labels: " + count_array);
        console.log("The array that holds the workouts ids:" + " " + graph);
        console.log("The object that holds the workouts and current authenticated users id: ");

        console.log(myData);

        var userName = document.getElementById("u-name").innerHTML;
        var context = document.getElementById('myWorkouts').getContext('2d');

        var myChart = new Chart(context, {
            type: 'bar',
            data: {
                labels: ["All users"],
                datasets: [{
                    label: '# of Workouts from all users',
                    data: [count],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
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