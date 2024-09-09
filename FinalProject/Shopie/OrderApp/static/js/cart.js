$(document).ready(function() {
        $('.quantity-plus').on('click', function() {
            var $button = $(this);
            var productId = $button.attr('product-id');
            var cartId = $button.attr('cart-id');
            var checkQuantityUrl = $button.attr('check-quantity-url');
            var $quantityElement = $button.siblings('.quantity');
            var quantity = parseInt($quantityElement.text());
            console.log(quantity)
            console.log(productId)
            console.log(cartId)
            console.log(checkQuantityUrl)
            $.ajax({
                url: checkQuantityUrl,
                data: {
                    'quantity': quantity,
                    'productId': productId,
                    'cartId': cartId
                },
                dataType: 'json',
                success: function (data) {
                    console.log(data)
                    if (data.state) {
                        $quantityElement.text(data['quantity']);
                    } else {
                        alert('Sorry, we have only ' + data['quantity'] + ' items in stock');
                    }
                }
            });
        });
    $('.quantity-minus').on('click', function () {
            var $button = $(this);
            var productId = $button.attr('product-id');
            var cartId = $button.attr('cart-id');
            var checkQuantityUrl = $button.attr('check-quantity-url');
            var $quantityElement = $button.siblings('.quantity');
            console.log(productId)
            console.log(cartId)
            console.log(checkQuantityUrl)
            
            $.ajax({
                url: checkQuantityUrl,
                data: {
                    'productId': productId,
                    'cartId': cartId
                },
                dataType: 'json',
                success: function (data) {
                    console.log(data)
                    if (data.state) {
                        $quantityElement.text(data['quantity']);
                    } else {
                        $('#' + productId).remove();
                        location.reload();
                    }
                },
                error: function(jqXHR, textStatus, errorThrown) {
                    console.error('AJAX Error:', textStatus, errorThrown);
                }
            });
        });
});