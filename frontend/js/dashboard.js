document.addEventListener('DOMContentLoaded', () => {
  // Pie Chart Configuration
  const ctxPie = document.getElementById('pieChart').getContext('2d');
  const pieChart = new Chart(ctxPie, {
    type: 'pie',
    data: {
      labels: ['Active', 'Inactive'],
      datasets: [{
        data: [60, 40], // Example data
        backgroundColor: ['#507687', '#B8001F'],
        hoverBackgroundColor: ['#386080', '#A7001B']
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        tooltip: {
          enabled: true,
        },
      }
    }
  });

  // Bar Chart Configuration
  const ctxBar = document.getElementById('barChart').getContext('2d');
  const barChart = new Chart(ctxBar, {
    type: 'bar',
    data: {
      labels: ['January', 'February', 'March'], // Example labels
      datasets: [{
        label: 'Entries',
        data: [10, 20, 15], // Example data
        backgroundColor: ['#507687', '#507687', '#507687'],
        hoverBackgroundColor: ['#386080', '#386080', '#386080']
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          display: true,
          position: 'top',
        },
        tooltip: {
          enabled: true,
        },
      },
      scales: {
        x: {
          title: {
            display: true,
            text: 'Months'
          }
        },
        y: {
          title: {
            display: true,
            text: 'Entries'
          },
          beginAtZero: true
        }
      }
    }
  });
});
