import paypalrestsdk
import datetime
import time
# This function is for getting the API IDs and Secrets
def getData(data):
    file_path = f"{data}"  
    try:
        with open(file_path, "r") as file:
            # Read the entire file content
            API_Data = file.read()
        
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return API_Data





# Set  PayPal API credentials
paypalrestsdk.configure({
    "mode": "sandbox",  # or "live" for production
    "client_id": getData("D:\CurrentClasses\Python\Sandbox_ID.txt"),
    "client_secret": getData("D:\CurrentClasses\Python\Sandbox_Secret.txt"),
})

#.....................................................................................................
transactions = paypalrestsdk.Payout
print(transactions)
payments = paypalrestsdk.Payment.all(params={"count": 1, "sort_by": "create_time", "sort_order": "desc"})
print(payments)
    # Check if there are payments
if payments and payments.success() and payments.payments:
    last_payment = payments.payments[0]
    create_time = last_payment.create_time  # Creation time of the last payment
    amount = last_payment.transactions[0].amount  # Amount of the last payment
        
    # Convert the creation time to readable format
    create_time_formatted = datetime.datetime.strptime(create_time, "%Y-%m-%dT%H:%M:%SZ")
        
    print(f"Last Payment Time: {create_time_formatted}")
    print(f"Last Payment Amount: {amount['total']} {amount['currency']}")
else:
    if payments.error:
        print(f"Error: {payments.error}")
    else:
        print("No transactions found.")
    #.................................................................................................