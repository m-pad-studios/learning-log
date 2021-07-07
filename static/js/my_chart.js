"use strict";

(function () {
  let context_2 = document.getElementById("myChart").getContext("2d");

  let key_2 = "topics";
  let graph_2 = [topics[key_2]];
  let count_2 = 0;
  let count_array_2 = [];

  for (let i = 0; i < graph_2[0].length; i++) {
    graph_2[i] = topics[key_2];
    count_2 += 1;
  }

  let key = "workouts";
  let current_user = "logged_user";
  let context = document.getElementById("myChart").getContext("2d");

  let graph = [myData[key]];
  let count = 0;
  let count_array = [];

  for (let i = 0; i < graph.length; i++) {
    graph[i] = myData[key];
  }

  for (let i = 0; i < graph[0].length; i++) {
    //  console.log(count);
    count_array[i] = count;
    count += 1;
  }

  let myChart = new Chart(context, {
    type: "bar",
    data: {
      labels: ["All workouts", "All topics"],
      datasets: [
        {
          label: "# of Workouts & Topics from all users",
          data: [count, count_2],
          backgroundColor: [
            "rgba(34, 139, 34, 0.5)",
            "rgba(54, 162, 235, 0.5)",
          ],
          borderColor: [
            "rgb(0, 0, 0)",
            "rgb(0, 0, 0)",
            "rgb(0, 0, 0)",
            "rgb(0, 0, 0)",
            "rgb(0, 0, 0)",
            "rgb(0, 0, 0)",
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
