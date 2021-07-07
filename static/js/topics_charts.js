"use strict";

(function () {
  //Bring in data from view JSon response
  let key = "polls_color";
  let graph_2 = [topics_2[key]];
  let votes_array = [];

  //Num of votes for each choice
  let bv = graph_2[0]["votes"][0];
  let rv = graph_2[0]["votes"][1];
  let gv = graph_2[0]["votes"][2];
  let ov = graph_2[0]["votes"][3];
  let pv = graph_2[0]["votes"][4];
  let yv = graph_2[0]["votes"][5];
  let blv = graph_2[0]["votes"][6];
  let wv = graph_2[0]["votes"][7];
  let pv_v = graph_2[0]["votes"][8];

  //Define colors for labels
  let blue = graph_2[0]["blue"];
  let red = graph_2[0]["red"];
  let green = graph_2[0]["green"];
  let orange = graph_2[0]["orange"];
  let purple = graph_2[0]["purple"];
  let yellow = graph_2[0]["yellow"];
  let black = graph_2[0]["black"];
  let white = graph_2[0]["white"];
  let pink = graph_2[0]["pink"];

  console.log(topics);
  for (let i = 0; i < graph_2[0].length; i++) {
    graph_2[i] = myData[key];
  }

  for (let i = 0; i < graph_2[0].length; i++) {
    count += 1;
    console.log(count);
    count_array.push(count);
  }

  console.log(graph_2);
  let myChart = new Chart(context, {
    type: "bar",
    data: {
      labels: [blue, red, green, orange, yellow, purple, white, black, pink],
      datasets: [
        {
          label: "Colors Poll",
          data: [bv, rv, gv, ov, yv, pv, wv, blv, pv_v],
          backgroundColor: [
            "rgb(0, 0, 255)",
            "rgb(255, 0, 0)",
            "rgb(60, 179, 113)",
            "rgb(255, 165, 0)",
            "rgb(255, 255, 0)",
            "rgb(106, 90, 205)",
            "rgb(255, 255, 255)",
            "rgb(0, 0, 0)",
            "rgb(254,184,198)",
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
