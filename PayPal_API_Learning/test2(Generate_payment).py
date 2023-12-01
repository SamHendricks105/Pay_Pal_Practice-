import paypalrestsdk
import datetime
import time
def getData(data):
    file_path = f"{data}"  # Replace with the path to your file
    try:
        with open(file_path, "r") as file:
            # Read the entire file content
            API_KEY = file.read()
        
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return API_KEY




# Set your PayPal API credentials
paypalrestsdk.configure({
    "mode": "sandbox",  # or "live" for production
    "client_id": getData("D:\CurrentClasses\Python\Sandbox_ID.txt"),
    "client_secret": getData("D:\CurrentClasses\Python\Sandbox_Secret.txt"),
})
#..........................................................................................................
# Create a test payment
payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "paypal",
    },
    "transactions": [{
        "amount": {
            "total": "10.00",
            "currency": "USD",
        },
        "description": "Test payment description.",
        "item_list": {
            "items": [{
                "name": "Test Item",
                "sku": "123",
                "price": "10.00",
                "currency": "USD",
                "quantity": 1,
            }],
        },
    }],
    "redirect_urls": {
        "return_url": "http://example.com/success",
        "cancel_url": "http://example.com/cancel",
    },
})

# Create and execute the payment
if payment.create():
    print("Payment created successfully")
    # Obtain approval URL and redirect the user to it for payment approval
    approval_url = [link.href for link in payment.links if link.rel == "approval_url"][0]
    print("Redirect the buyer to the following URL to approve the payment:")
    print(approval_url)
else:
    print("Error creating payment:")
    print(payment.error)

#..........................................................................................................
# Retrieve the last payment
import time

# ... (Your existing code for creating the payment)

# Introduce a longer delay (e.g., 10 seconds). Adjust as needed.
time.sleep(10)

# Wait for the payment to be processed and retrieve the last payment
max_retries = 2
retry_count = 0

while True:
    payments = paypalrestsdk.Payment.all(params={"count": 1, "sort_by": "create_time", "sort_order": "desc"})
    if payments and payments.success() and payments.payments:
        # Payment found, break out of the loop
        break
    elif payments.error:
        print(f"Error: {payments.error}")
        break
    elif retry_count < max_retries:
        # Retry after a delay if the payment is not yet processed
        retry_count += 1
        print(f"Retry {retry_count}/{max_retries} - Waiting for payment processing...")
        time.sleep(10)  # Adjust the delay as needed
    else:
        print("Max retries reached. No transactions found.")
        break

# Check if there are payments
if payments and payments.success() and payments.payments:
    #.....................................................................................................
    payments = paypalrestsdk.Payment.all(params={"count": 1, "sort_by": "create_time", "sort_order": "desc"})
    print(payments)
    # Check if there are payments
    if payments and payments.success() and payments.payments:
        last_payment = payments.payments[0]
        create_time = last_payment.create_time  # Creation time of the last payment
        amount = last_payment.transactions[0].amount  # Amount of the last payment
        
        # Convert the creation time to a human-readable format
        create_time_formatted = datetime.datetime.strptime(create_time, "%Y-%m-%dT%H:%M:%SZ")
        
        print(f"Last Payment Time: {create_time_formatted}")
        print(f"Last Payment Amount: {amount['total']} {amount['currency']}")
    else:
        if payments.error:
            print(f"Error: {payments.error}")
        else:
            print("No transactions found.")
    #.................................................................................................



#.....................................................................................................
payments = paypalrestsdk.Payment.all(params={"count": 1, "sort_by": "create_time", "sort_order": "desc"})
print(payments)
# Check if there are payments
if payments and payments.success() and payments.payments:
    last_payment = payments.payments[0]
    create_time = last_payment.create_time  # Creation time of the last payment
    amount = last_payment.transactions[0].amount  # Amount of the last payment
    
    # Convert the creation time to a human-readable format
    create_time_formatted = datetime.datetime.strptime(create_time, "%Y-%m-%dT%H:%M:%SZ")
    
    print(f"Last Payment Time: {create_time_formatted}")
    print(f"Last Payment Amount: {amount['total']} {amount['currency']}")
else:
    if payments.error:
        print(f"Error: {payments.error}")
    else:
        print("No transactions found.")
#.................................................................................................