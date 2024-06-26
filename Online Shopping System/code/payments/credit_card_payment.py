from payments.payment_method import PaymentMethod

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount: float) -> bool:
        return True
