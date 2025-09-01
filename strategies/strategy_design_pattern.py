from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class CreditCardPayment(Payment):
    def pay(self,amount):
        return f"Paying {amount} through Credit Card"
class PayPalPayement(Payment):
    def pay(self,amount):
        return f"Paying {amount} through PayPal"
class BitcoinPayment(Payment):
    def pay(self,amount):
        return f"Paying {amount} through Bitcoin"
class shoppingcart:
    def __init__(self,paymentmethod):
        self.payment_method=paymentmethod
    def checkout(self,amount):
        return self.payment_method.pay(amount)
    
if __name__=="main":
    cart=shoppingcart(CreditCardPayment())
    print(cart.checkout(100))
    cart=shoppingcart(BitcoinPayment())
    print(cart.checkout(300))
    cart=shoppingcart(PayPalPayement())
    print(cart.checkout(500))