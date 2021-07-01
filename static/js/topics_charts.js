"use strict";
        
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

    (function() {

   //Bring in data from view JSon response
   var key = "polls_color";
   var graph_2 = [topics_2[key]];
   var votes_array = [];

   //Num of votes for each choice
   var bv = graph_2[0]['votes'][0]
   var rv = graph_2[0]['votes'][1]
   var gv = graph_2[0]['votes'][2]
   var ov = graph_2[0]['votes'][3]
   var pv = graph_2[0]['votes'][4]
   var yv = graph_2[0]['votes'][5]
   var blv = graph_2[0]['votes'][6]
   var wv = graph_2[0]['votes'][7]

   //Define colors for labels
   var blue = graph_2[0]['blue']
   var red = graph_2[0]['red']
   var green = graph_2[0]['green']
   var orange = graph_2[0]['orange']
   var purple = graph_2[0]['purple']
   var yellow = graph_2[0]['yellow']
   var black = graph_2[0]['black']
   var white = graph_2[0]['white']

  
   console.log(topics);
   for(var i = 0; i < graph_2[0].length; i++)
   {
       graph_2[i] = myData[key];
    

   }

   for(var i = 0; i < graph_2[0].length; i++) {
       count += 1;
       console.log(count);
       count_array.push(count);
     
   }

console.log(graph_2);
   var myChart = new Chart(context, {
       type: 'bar',
       data: {
           labels: [blue, red, green, orange, yellow, purple, white, black],
           datasets: [{
               label: "Colors Poll",
               data: [bv,rv,gv,ov,yv,pv,wv,blv],
               backgroundColor: [
                   'rgb(0, 0, 255)',
                   'rgb(255, 0, 0)',
                   'rgb(60, 179, 113)',
                   'rgb(255, 165, 0)',
                   'rgb(255, 255, 0)',
                   'rgb(106, 90, 205)',
                   'rgb(255, 255, 255)',
                   'rgb(0, 0, 0)'
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
    })();
     