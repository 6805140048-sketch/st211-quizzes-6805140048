from shopping import ShoppingCart

class TestShoppingCart:
    def test_new_cart_is_empty(self):
        cart = ShoppingCart()
        assert cart.count() == 0

    def test_new_cart_total_is_zero(self):
        cart = ShoppingCart()
        assert cart.total() == 0

    def test_add_item_increases_count(self):
        cart = ShoppingCart()
        cart.add("Book", 20)
        cart.add("Pencil", 3)
        cart.add("Mirror", 30)
        assert cart.count() == 3

    def test_total_sums_prices(self):
        cart = ShoppingCart()
        cart.add("Book", 20)
        cart.add("Pen", 5)
        cart.add("Car", 200000)
        assert cart.total() == 200025

    
    
