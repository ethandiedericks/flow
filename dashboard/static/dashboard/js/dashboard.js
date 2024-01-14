document.addEventListener("DOMContentLoaded", function() {
  var bigChartCanvas = document.getElementById('bigChart');
  var bigChartType = 'line';
  var bigChart;

  function updateBigChart() {
      // Implement logic to fetch data for bigChart based on the selected dropdown item
      // For simplicity, I'll use dummy data here
      var bigChartData;

      if (bigChartType === 'line') {
          bigChartData = {
              labels: ['Category 1', 'Category 2', 'Category 3'],
              datasets: [
                  {
                      label: 'Income',
                      data: [500, 200, 300],
                      borderColor: 'rgba(75, 192, 192, 1)',
                      borderWidth: 2,
                      fill: false
                  },
                  {
                      label: 'Expenses',
                      data: [100, 150, 50],
                      borderColor: 'rgba(255, 99, 132, 1)',
                      borderWidth: 2,
                      fill: false
                  },
                  {
                      label: 'Investments',
                      data: [200, 100, 400],
                      borderColor: 'rgba(255, 205, 86, 1)',
                      borderWidth: 2,
                      fill: false
                  }
              ]
          };
      } else if (bigChartType === 'bar') {
          // Dummy data for bar chart
          bigChartData = {
              labels: ['Category 1', 'Category 2', 'Category 3'],
              datasets: [
                  {
                      label: 'Amount',
                      data: [1000, 500, 700],
                      backgroundColor: ['rgba(75, 192, 192, 0.2)', 'rgba(255, 99, 132, 0.2)', 'rgba(255, 205, 86, 0.2)'],
                      borderColor: ['rgba(75, 192, 192, 1)', 'rgba(255, 99, 132, 1)', 'rgba(255, 205, 86, 1)'],
                      borderWidth: 1
                  }
              ]
          };
      }

      var bigChartOptions = {
          scales: {
              y: {
                  beginAtZero: true
              }
          }
      };

      // Destroy the existing chart if it exists
      if (bigChart) {
          bigChart.destroy();
      }

      // Create a new chart instance for bigChart
      bigChart = new Chart(bigChartCanvas, {
          type: bigChartType,
          data: bigChartData,
          options: bigChartOptions
      });
  }

  // Initial chart rendering
  updateBigChart();

  // Event listeners for bigChart dropdown
  document.querySelector('.line-dropdown-item').addEventListener('click', function() {
      bigChartType = 'line';
      updateBigChart();
  });

  document.querySelector('.bar-dropdown-item').addEventListener('click', function() {
      bigChartType = 'bar';
      updateBigChart();
  });
  var smallChartCanvas = document.getElementById('smallChart');
  var smallChartType = 'doughnut';
  var smallChart;

  function updateSmallChart() {
      // Implement logic to fetch data for smallChart based on the selected dropdown item
      // For simplicity, I'll use dummy data here
      var smallChartData;

      if (smallChartType === 'doughnut') {
          smallChartData = {
              labels: ['Category 1', 'Category 2', 'Category 3'],
              datasets: [{
                  data: [300, 150, 200],
                  backgroundColor: ['rgba(75, 192, 192, 0.2)', 'rgba(255, 99, 132, 0.2)', 'rgba(255, 205, 86, 0.2)'],
                  borderColor: ['rgba(75, 192, 192, 1)', 'rgba(255, 99, 132, 1)', 'rgba(255, 205, 86, 1)'],
                  borderWidth: 1
              }]
          };
      } else if (smallChartType === 'pie') {
          smallChartData = {
              labels: ['Category 1', 'Category 2', 'Category 3'],
              datasets: [{
                  data: [200, 100, 300],
                  backgroundColor: ['rgba(75, 192, 192, 0.2)', 'rgba(255, 99, 132, 0.2)', 'rgba(255, 205, 86, 0.2)'],
                  borderColor: ['rgba(75, 192, 192, 1)', 'rgba(255, 99, 132, 1)', 'rgba(255, 205, 86, 1)'],
                  borderWidth: 1
              }]
          };
      }

      var smallChartOptions = {
          scales: {
              y: {
                  beginAtZero: true
              }
          }
      };

      // Destroy the existing chart if it exists
      if (smallChart) {
          smallChart.destroy();
      }

      // Create a new chart instance for smallChart
      smallChart = new Chart(smallChartCanvas, {
          type: smallChartType,
          data: smallChartData,
          options: smallChartOptions
      });
  }

  // Initial chart rendering
  updateSmallChart();

  // Event listeners for smallChart dropdown
  document.querySelector('.doughnut-dropdown-item').addEventListener('click', function() {
      smallChartType = 'doughnut';
      updateSmallChart();
  });

  document.querySelector('.pie-dropdown-item').addEventListener('click', function() {
      smallChartType = 'pie';
      updateSmallChart();
  });

});