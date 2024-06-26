from payments.payment_method import PaymentMethod

class CashOnDelivery(PaymentMethod):
    def process_payment(self, amount: float) -> bool:
        return True
