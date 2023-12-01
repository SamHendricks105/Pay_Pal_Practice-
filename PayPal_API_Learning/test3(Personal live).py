import paypalrestsdk
import logging
# This function is for getting the API IDs and Secrets
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
    "mode": "live",  # or "live" for production
    "client_id": getData("D:\CurrentClasses\Python\personal_live_id.txt") ,
    "client_secret": getData("D:\CurrentClasses\Python\personal_live_secret"),
})

# Create a Payout
payout = paypalrestsdk.Payout({
    "sender_batch_header": {
        "sender_batch_id": "batch_12345",
        "email_subject": "You have a payment",
    },
    "items": [
        {
            "recipient_type": "EMAIL",
            "amount": {
                "value": "1.0",
                "currency": "USD",
            },
            "receiver": "recipient@example.com",
            "note": "Thank you.",
            "sender_item_id": "item_1",
        }
        # Add more items for additional recipients if needed
    ],
})

# Create and execute the Payout
if payout.create(sync_mode=False):  # Set sync_mode to True for synchronous processing
    print(f"Payout batch id:{payout.batch_header.payout_batch_id}")
else:
    print(f"Error creating payout: {payout.error}")

# Log the details for debugging
logging.basicConfig(level=logging.INFO)
logging.info(payout.to_dict())
