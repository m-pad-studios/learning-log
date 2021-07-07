"use strict";

(function () {
  let key_2 = "my_stats";
  let graph_3 = [my_info[key_2]];

  let count_2 = 0;
  let count_array_2 = [];

  let topic_data = graph_3[0][0];

  let workout_data = graph_3[0][1];

  let myChart = new Chart(context, {
    type: "pie",
    data: {
      labels: [
        "All " + userName + "'s' workouts",
        "All " + userName + "'s  topics",
      ],
      datasets: [
        {
          label: "# of Workouts & Topics from",
          data: [workout_data.length, topic_data.length],
          backgroundColor: [
            "rgba(34, 139, 34, 0.5)",
            "rgba(54, 162, 235, 0.5)",
            "rgba(255, 206, 86, 0.5)",
            "rgba(75, 192, 192, 0.5)",
            "rgba(153, 102, 255, 0.5)",
            "rgba(255, 159, 64, 0.5)",
          ],
          borderColor: [
            "rgb(0, 0, 0)",
            "rgb(0, 0, 0)",
            "rgb(0, 0, 0)",
            "rgba(75, 192, 192, 1)",
            "rgba(153, 102, 255, 1)",
            "rgba(255, 159, 64, 1)",
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
})();
