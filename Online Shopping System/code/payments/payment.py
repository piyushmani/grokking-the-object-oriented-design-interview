from dataclasses import dataclass
from payments.payment_method import PaymentMethod

@dataclass
class Payment:
    amount: float
    method: PaymentMethod
