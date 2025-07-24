from .signals import payment_completed

def complete_payment(order_id, amount):
    """
    Function to complete a payment and send a signal.
    """
    # Logic to complete the payment goes here
    print(f"App TEST_PACKAGE đã bắn đi tín hiệu Signal: Payment completed for order {order_id} with amount {amount}")

    # Send the signal after completing the payment
    payment_completed.send(sender=None, order_id=order_id, amount=amount)