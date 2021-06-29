
        
    $("#fading").click(function () {



        $("#div1").fadeIn();
        $("#div2").fadeIn();
        $("#div3").fadeIn();
        $("#div4").fadeIn();

    });

    $("#fadingOut").click(function () {



        $("#div1").fadeOut();
        $("#div2").fadeOut();
        $("#div3").fadeOut();
        $("#div4").fadeOut();



    });
        
        var key = "topic";
        var graph_2 = [topics_2[key]];
        var count = 0;
        var count_array = [];
        console.log(topics);
        for(var i = 0; i < graph_2.length; i++)
        {
            graph_2[i] = myData[key];

        }

        for(var i = 0; i < graph_2[0].length; i++) {
            count += 1;
            console.log(count);
            count_array[i] = count;
        }


        var myChart = new Chart(context, {
            type: 'bar',
            data: {
                labels: ["All topics"],
                datasets: [{
                    label: '# of Topics from all users',
                    data: [count],
                    backgroundColor: [
                        'rgba(135,206,235, 0.5)',
                        'rgba(135,206,235, 0.5)',
                        'rgba(135,206,235, 0.5)',
                        'rgba(135,206,235, 0.5)',
                        'rgba(135,206,235, 0.5)',
                        'rgba(135,206,235, 0.5)'
                    ],
                    borderColor: [
                        'rgba(135,206,235, 1)',
                        'rgba(135,206,235, 1)',
                        'rgba(135,206,235, 1)',
                        'rgba(135,206,235, 1)',
                        'rgba(135,206,235, 1)',
                        'rgba(135,206,235, 1)'
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