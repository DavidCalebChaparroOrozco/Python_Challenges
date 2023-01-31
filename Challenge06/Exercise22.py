# Create a function to calculate the total of a payment including an applied tax.
# Formula: total_payment = payment_without_tax + payment_without_tax * (tax/100)
def calculate_total_payment(payment, tax) -> float:
    return payment + payment * (tax / 100)

payment = float(input("Enter payment amount: "))
tax = float(input("Enter tax rate (in %): "))
total_payment = calculate_total_payment(payment, tax)
print("Total payment: ", total_payment)