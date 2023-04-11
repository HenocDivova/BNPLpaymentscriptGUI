import tkinter as tk


class PaymentApp(tk.Tk):
    def __init__(self, total_amount, num_installments):
        super().__init__()
        self.title("Payment App")
        self.geometry("300x150")

        self.total_amount = total_amount
        self.num_installments = num_installments
        self.installment_amount = total_amount / num_installments
        self.installments_made = 0

        # Create a label to display the installment amount
        self.installment_label = tk.Label(self, text="Installment amount: $%.2f" % self.installment_amount)
        self.installment_label.pack()

        # Create a text entry box for the user to enter payment amounts
        self.payment_entry = tk.Entry(self)
        self.payment_entry.pack()

        # Create a button to submit the payment
        self.submit_button = tk.Button(self, text="Submit Payment", command=self.submit_payment)
        self.submit_button.pack()

    def submit_payment(self):
        # Get the payment amount from the user
        payment = self.payment_entry.get()
        payment = float(payment)

        # Check if the payment is valid (i.e. less than or equal to the remaining amount due)
        if payment <= self.total_amount:
            # Update the total amount due and the number of installments made
            self.total_amount -= payment
            self.installments_made += 1

            # Update the installment label to reflect the new total amount due
            self.installment_label.configure(
                text="Installment amount: $%.2f" % (self.total_amount / self.num_installments))

            # Clear the payment entry box
            self.payment_entry.delete(0, "end")

            # If the total amount has been paid, display a message to the user
            if self.total_amount == 0:
                tk.Label(self, text="Payments complete. Total installments made: %d" % self.installments_made).pack()
                self.submit_button.configure(state="disabled")
        else:
            tk.Label(self, text="Invalid payment amount. Please try again.").pack()


# Example usage: create a PaymentApp to make a payment of $100 in 5 installments
app = PaymentApp(100, 5)
app.mainloop()
