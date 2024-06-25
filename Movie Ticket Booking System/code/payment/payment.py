from dataclasses import dataclass

@dataclass
class Payment:
    amount: float
    method: "PaymentMethod"

    def process(self) -> bool:
        return self.method.process_payment(self.amount)
