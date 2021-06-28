var topics = {{ serialized_data | safe}};
var key = "topic";
var graph = [topics[key]];
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
    type: 'line',
    data: {
        labels: ["All topics"],
        datasets: [{
            label: '# of Topics from all users',
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
