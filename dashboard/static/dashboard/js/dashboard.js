async function fetchData(url) {
    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        return await response.json();
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
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
// handle edit and delete operations on table data
$(document).ready(function () {
    var transID = "";
    $('.transaction-row').click(function () {
        var transactionId = $(this).data('transaction-id');
        transID = transactionId;
        var modalBody = $('#editTransactionModalBody');

        // Use AJAX to fetch the form HTML from the server
        $.ajax({
            type: 'GET',
            url: 'edit-transaction/' + transactionId + '/fetch/',
            success: function (data) {
                // Update the modal body with the fetched form HTML
                modalBody.html(data);
            },
            error: function (error) {
                console.log('Error fetching form: ', error);
            }
        });
    });
    // Handle the form submission event
    $('#editTransactionModalBody').on('submit', '#editTransactionForm', function (e) {
        e.preventDefault();

        var form = $(this);
        var formData = form.serialize();

        // Check if the delete button is selected
        var deleteTransaction = form.find('#id_delete').prop('checked');

        if (deleteTransaction) {
            // Perform delete action
            if (confirm('Are you sure you want to delete this transaction?')) {
                $.ajax({
                    type: 'POST',
                    url: form.attr('action'),
                    data: formData,
                    success: function (data) {
                        console.log('Transaction deleted successfully:', data);
                        $('#editTransactionModal').modal('hide');
                        location.reload();
                    },
                    error: function (xhr, status, error) {
                        console.error('AJAX error:', status, error);
                        console.log(xhr.responseText);
                    }
                });
            }
        } else {
            // Perform update action
            $.ajax({
                type: 'POST',
                url: form.attr('action'),
                data: formData,
                success: function (data) {
                    console.log('Transaction updated successfully:', data);
                    $('#editTransactionModal').modal('hide');
                    location.reload();
                },
                error: function (xhr, status, error) {
                    console.error('AJAX error:', status, error);
                    console.log(xhr.responseText);

                    // Display server-side validation errors
                    var errors = JSON.parse(xhr.responseText);
                    for (var field in errors) {
                        var errorMessage = errors[field][0];
                        alert(errorMessage);
                    }
                }
            });
        }
    });

    // Handle the delete button click event
    $('#editTransactionModalBody').on('click', '#deleteTransactionBtn', function () {
        // Open the delete confirmation modal
        var transactionId = transID;
        var deleteModalUrl = 'edit-transaction/' + transactionId + '/delete/';
        
        console.log('Transaction ID:', transactionId);
        $.get(deleteModalUrl, function (data) {
            // Replace the content of the delete confirmation modal body with the new data
            $('#deleteTransactionModal .modal-body').html(data);
            // Hide edit modal
            $('#editTransactionModal').modal('hide');
            // Show the delete confirmation modal
            $('#deleteTransactionModal').modal('show');
        });
    });

    
    // Handle the delete confirmation form submission event
    $('body').on('submit', '#deleteTransactionForm', function (e) {
        e.preventDefault();
        
        var deleteForm = $(this);
        var deleteFormData = deleteForm.serialize();
        
        // Perform delete action
        $.ajax({
            type: 'POST',
            url: deleteForm.attr('action'),
            data: deleteFormData,
            success: function (data) {
                console.log('Transaction deleted successfully:', data);
                $('#deleteTransactionModal').modal('hide');
                location.reload();
            },
            error: function (xhr, status, error) {
                console.error('AJAX error:', status, error);
                console.log(xhr.responseText);
            }
        });
    });
});
