from Entities.Payment import Payment
from Infrastructure.PaymentRepository import PaymentRepository

class ProcessPaymentUseCase:
    def __init__(self, payment_repository: PaymentRepository):
        self.payment_repository = payment_repository

    def execute(self, order_id: int, amount: float, payment_date: str, status: str) -> str:
        new_payment = Payment(order_id=order_id, amount=amount, payment_date=payment_date, status=status)
        self.payment_repository.save(new_payment)
        return "Payment processed successfully."
