
# class Beverage():
#     """
#     The base Component interface defines operations that can be altered by
#     decorators.
#     """

#     def desc(self):
#         pass

#     def cost(self):
#         pass

# class Coffee(Beverage):
#     """
#     Concrete Components provide default implementations of the operations. There
#     might be several variations of these classes.
#     """

#     def desc(self):
#         return "Coffee"

#     def cost(self):
#         return 3

# class Decorator(Beverage):
#     """
#     The base Decorator class follows the same interface as the other components.
#     The primary purpose of this class is to define the wrapping interface for
#     all concrete decorators. The default implementation of the wrapping code
#     might include a field for storing a wrapped component and the means to
#     initialize it.
#     """

#     def __init__(self, beverage):
#         self._beverage = beverage

#     @property
#     def beverage(self):
#         return self._beverage

#     def desc(self):
#         self._beverage.desc()

#     def cost(self):
#         self._beverage.cost()


# class Milk(Decorator):
#     """
#     Concrete Decorators call the wrapped object and alter its result in some
#     way.
#     """

#     def desc(self):
#         """
#         Decorators may call parent implementation of the operation, instead of
#         calling the wrapped object directly. This approach simplifies extension
#         of decorator classes.
#         """
#         return 'Milk' + self.beverage.desc()

#     def cost(self):
#     	return 1 + self.beverage.cost()


# class Sugar(Decorator):
#     """
#     Decorators can execute their behavior either before or after the call to a
#     wrapped object.
#     """

#     def desc(self):
#         return 'Sugar' + self.beverage.desc()

#     def cost(self):
#     	return 2 + self.beverage.cost()



# if __name__ == "__main__":
#     # This way the client code can support both simple components...
#     simple = Coffee()
#     print(simple.desc())

#     # ...as well as decorated ones.
#     #
#     # Note how decorators can wrap not only simple components but the other
#     # decorators as well.
#     decorator1 = Milk(simple)
#     decorator2 = Sugar(decorator1)
#     print(decorator2.desc())
#     cof = Coffee()
#     # cof = Milk(cof)
#     cof = Sugar(cof)
#     print(cof.desc())
#     print(cof.cost())


# Works using python decarators
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order: # the Context

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

promos = []
def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
    """7% discount for orders with 10 or more distinct items""" 
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order):
    # Select best discount available
    return max(promo(order) for promo in promos)


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
# long_order = [LineItem(str(item_code), 1, 1.0) ... for item_code in range(10)]
banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermellon', 5, 5.0)]
# Order(joe, long_order, best_promo)
    # <Order total: 10.00 due: 9.30>
print(Order(joe, banana_cart, best_promo))
    # <Order total: 30.00 due: 28.50>
print(Order(ann, cart, best_promo))
    # <Order total: 42.00 due: 39.90>



