function fetchData(url) {
    return fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}
document.addEventListener("DOMContentLoaded", function () {
    var bigChart;  // Variable to store the bigChart instance
    var smallChart;  // Variable to store the smallChart instance

    function updateChart(chartId, chartType) {
        fetchData("get_totals/").then((totalsData) => {
            var labels = ["Incomes", "Expenses", "Investments"];
            var values = [totalsData.total_incomes, totalsData.total_expenses, totalsData.total_investments];

            // Destroy existing chart instance if it exists
            if (chartId === "bigChart" && bigChart) {
                bigChart.destroy();
            } else if (chartId === "smallChart" && smallChart) {
                smallChart.destroy();
            }

            // Render the new chart
            renderChart(chartId, chartType, labels, values);
        });
    }

    function renderChart(chartId, type, labels, values) {
        var ctx = document.getElementById(chartId).getContext("2d");

        // Create a new Chart instance and store it in the appropriate variable
        if (chartId === "bigChart") {
            bigChart = new Chart(ctx, {
                type: type,
                data: {
                    labels: labels,
                    datasets: [{
                        data: values,
                        backgroundColor: [
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(255, 205, 86, 0.2)',
                        ],
                        borderColor: [
                            'rgba(75, 192, 192, 1)',
                            'rgba(255, 99, 132, 1)',
                            'rgba(255, 205, 86, 1)',
                        ],
                        borderWidth: 1,
                    }],
                },
            });
        } else if (chartId === "smallChart") {
            smallChart = new Chart(ctx, {
                type: type,
                data: {
                    labels: labels,
                    datasets: [{
                        data: values,
                        backgroundColor: [
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(255, 205, 86, 0.2)',
                        ],
                        borderColor: [
                            'rgba(75, 192, 192, 1)',
                            'rgba(255, 99, 132, 1)',
                            'rgba(255, 205, 86, 1)',
                        ],
                        borderWidth: 1,
                    }],
                },
            });
        }
    }

    function updateBarChart() {
        fetchData("get_totals/").then((totalsData) => {
            var labels = ["Incomes", "Expenses", "Investments"];
            var incomeValues = totalsData.income_details.map(item => item.total_amount);
            var expenseValues = totalsData.expense_details.map(item => item.total_amount);
            var investmentValues = totalsData.investment_details.map(item => item.total_amount);

            if (bigChart) {
                bigChart.destroy();
            }

            renderBarChart("bigChart", labels, incomeValues, expenseValues, investmentValues);
        });
    }

    function renderBarChart(chartId, labels, incomeValues, expenseValues, investmentValues) {
        var ctx = document.getElementById(chartId).getContext("2d");
        
        bigChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Income',
                    data: incomeValues,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                }, {
                    label: 'Expense',
                    data: expenseValues,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1,
                }, {
                    label: 'Investment',
                    data: investmentValues,
                    backgroundColor: 'rgba(255, 205, 86, 0.2)',
                    borderColor: 'rgba(255, 205, 86, 1)',
                    borderWidth: 1,
                }],
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    // Event listeners for user selection change
    var smallChartType = document.getElementById("smallChartType");
    var bigChartType = document.getElementById("bigChartType");

    if (smallChartType) {
        smallChartType.addEventListener("change", function () {
            updateChart("bigChart", this.value);
        });
    }

    if (bigChartType) {
        bigChartType.addEventListener("change", function () {
            updateChart("smallChart", this.value);
        });
    }


    // Event listener for bar chart
    var barChartBtn = document.getElementById("barChartBtn");

    if (barChartBtn) {
        barChartBtn.addEventListener("click", updateBarChart);
    }

    // Initial chart rendering
    updateChart("bigChart", smallChartType ? smallChartType.value : 'line');
    updateChart("smallChart", bigChartType ? bigChartType.value : 'doughnut');
});
