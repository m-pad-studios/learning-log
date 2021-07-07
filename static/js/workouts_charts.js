"use strict";
(function () {
  let key = "workout";
  let current_user = "logged_user";

  let graph = [myData[key]];
  let count = 0;

  for (let i = 0; i < graph.length; i++) {
    graph[i] = myData[key];
    count += 1;
  }

  let userName = document.getElementById("u-name").innerHTML;
  let context = document.getElementById("myWorkouts").getContext("2d");

  let myChart = new Chart(context, {
    type: "bar",
    data: {
      labels: ["All users"],
      datasets: [
        {
          label: "# of Workouts from all users",
          data: [count],
          backgroundColor: [
            "rgba(5, 9, 132, 0.5)",
            "rgba(54, 162, 235, 0.5)",
            "rgba(255, 206, 86, 0.5)",
            "rgba(75, 192, 192, 0.5)",
            "rgba(153, 102, 255, 0.5)",
            "rgba(255, 159, 64, 0.5)",
          ],
          borderColor: [
            "rgb(0, 0, 0)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
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
