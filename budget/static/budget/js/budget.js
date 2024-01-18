$(document).ready(function() {

    // handle deletion
    $('.badge-btn').click(function(event) {
        event.preventDefault();

        var transactionId = $(this).data('transaction-id');
        var badgeContainer = $(this).closest('.badge-container');
        var totalsContainer = $('.totals-container'); 
        var legendContainer = $('.legend');

        $.ajax({
            type: 'POST',
            url: 'delete_transaction/' + transactionId + '/',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function(response) {
                if (response.message === 'Transaction deleted successfully') {
                    $('[data-transaction-id="' + transactionId + '"]').closest('.badge').remove();

                    // Fetch updated totals from the server
                    $.get('get_totals/', function(updatedTotals) {
                        // Update the HTML with the new totals
                        totalsContainer.find('.income-total').text(updatedTotals.income_total);
                        totalsContainer.find('.expense-total').text(updatedTotals.expense_total);
                        totalsContainer.find('.investment-total').text(updatedTotals.investment_total);

                        if (updatedTotals.income_total === 0 && updatedTotals.expense_total === 0 && updatedTotals.investment_total === 0) {
                            legendContainer.remove();
                            totalsContainer.remove();
                        }
                    });
                } else {
                    console.error('Error:', response.message);
                }
            },
            error: function() {
                console.error('AJAX error');
            },
        });
    });


});
