$(document).ready(function() {

    // Fetch initial totals from the server
    $.get('get_totals/', function(initialTotals) {
        updateTotals(initialTotals);

        // Hide totalsContainer if all initial totals are zero
        if (initialTotals.income_total === 0 && initialTotals.expense_total === 0 && initialTotals.investment_total === 0) {
            $('.totals-container').hide();
        }
    });
    
    // handle creation
    $('#transactionForm').submit(function(event) {
        event.preventDefault();

        var formData = $(this).serialize();

        $.ajax({
            type: 'POST',
            url: 'create_transaction/',
            data: formData,
            success: function(response) {
                if (response.message === 'Transaction created successfully') {
                    // Fetch updated totals from the server
                    $.get('get_totals/', function(updatedTotals) {
                        updateTotals(updatedTotals);
                    });

                    // Reset the form
                    $('#transactionForm')[0].reset();
                } else {
                    console.error('Error:', response.message);
                }
            },
            error: function(response) {
                // Handle form validation errors
                var errors = response.responseJSON.errors;
                displayFormErrors(errors);
            },
        });
    });


    function updateTotals(updatedTotals) {
        var totalsContainer = $('.totals-container');
    
        // Update the HTML with the new totals
        totalsContainer.find('.income-total').text(updatedTotals.income_total);
        totalsContainer.find('.expense-total').text(updatedTotals.expense_total);
        totalsContainer.find('.investment-total').text(updatedTotals.investment_total);
    
        // Show/hide legend and totals based on the values
        if (updatedTotals.income_total === 0 && updatedTotals.expense_total === 0 && updatedTotals.investment_total === 0) {
            totalsContainer.hide();
        } else {
            totalsContainer.show();
        }
    }
    

    function displayFormErrors(errors) {
        // Display form validation errors on the page
        for (var field in errors) {
            if (errors.hasOwnProperty(field)) {
                var errorMessage = errors[field][0];  // Display only the first error for simplicity
                // Assuming you have an element with the class 'form-error' to display the error
                $('.form-error-' + field).text(errorMessage);
            }
        }
    }

});
