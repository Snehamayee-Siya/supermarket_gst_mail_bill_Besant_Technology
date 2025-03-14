# INTERMEDIATE PYTHON  (day 18) (10.03.25) (4th assignment)
# Assignment -->

# Pass some Supermarket based data via api link
# get the data from json frormat using in python code
# validate the total amaount including gst and add some logic for the user giving name, mail id,etc and like how much apple or grocery he or she buy in kg or gram and add gst vallue and prepare the final amount bill
# ask the input for user "hey do u want to send a mail or generate the bill"
# if generate bill then just in text fromat give the bill or else send mail then logic to send bill through mail or to send the only final amount msg like "hey the total amount to pay is : 50000/-" like this.
# At the end do it inside a functionand also us ethe concept exception handling


import requests
import smtplib

def fetch_supermarket_data():
    try:
        url = "http://demo4306484.mockable.io/supermarket_data"
        response = requests.get(url)
        response.raise_for_status()
        get_data = response.json()
        return get_data.get("supermarket_items", [])
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def display_available_items(items):
    print("\nAvailable Products:")
    for item in items:
        print(f"{item['name']} - Rs. {item['price']} per kg/unit")

def calculate_bill(cart, gst_rate=0.18):
    total_amount = sum(item['price'] * item['quantity'] for item in cart)
    gst_amount = total_amount * gst_rate
    final_amount = total_amount + gst_amount
    return total_amount, gst_amount, final_amount

def send_email(to_email, name, cart, total, gst, final_amount):
    try:
        sender_email = "example@gmail.com"
        sender_password = "*********"
        
        subject = "Supermarket Bill Details"
        items_details = "\n".join([f"{item['name']}: {item['quantity']}kg/unit @ Rs.{item['price']}" for item in cart])
        message = (f"Subject: {subject}\n\n"
                   f"Hi {name},\n\n"
                   f"Here is your purchase summary:\n\n"
                   f"{items_details}\n\n"
                   f"Total Amount: Rs. {total:.2f}/-\n"
                   f"GST (18%): Rs. {gst:.2f}/-\n"
                   f"Final Amount: Rs. {final_amount:.2f}/-\n\n"
                   f"Thank you for shopping with us!")
        
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email, sender_password)
        s.sendmail(sender_email, to_email, message)
        s.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def generate_bill():
    data = fetch_supermarket_data()
    if not data:
        return
    
    display_available_items(data)
    
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    
    cart = []
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        
        try:
            quantity = float(input("Enter quantity (kg or grams): "))
            price = next((item['price'] for item in data if item['name'].lower() == item_name.lower()), None)
            
            if price is None:
                print("Item not found. Please try again.")
                continue
            
            cart.append({"name": item_name, "quantity": quantity, "price": price})
        except ValueError:
            print("Invalid input. Please enter a numeric value for quantity.")
    
    total, gst, final_amount = calculate_bill(cart)
    bill_text = (f"\nName: {name}\n"
                 f"\nItem Details:\n"
                 + "\n".join([f"{item['name']}: {item['quantity']}kg/unit @ Rs.{item['price']}" for item in cart]) + "\n"
                 f"\nTotal Amount: Rs. {total:.2f}/-\n"
                 f"GST (18%): Rs. {gst:.2f}/-\n"
                 f"Final Amount: Rs. {final_amount:.2f}/-")
    
    choice = input("Do you want to send a mail or generate a bill? (mail/bill): ")
    if choice.lower() == "mail":
        send_email(email, name, cart, total, gst, final_amount)
    else:
        print("\nFinal Bill:")
        print(bill_text)

if __name__ == "__main__":
    generate_bill()






























# import requests
# import smtplib

# def fetch_supermarket_data():
#     url = "http://demo4306484.mockable.io/supermarket_data"
#     response = requests.get(url)
#     get_data = response.json()
    
#     return get_data["supermarket_items"]

# def display_available_items(items):
#     print("\nAvailable Products:")
#     for item in items:
#         print(f"{item['name']} - Rs. {item['price']} per kg/unit")

# def calculate_bill(cart, gst_rate=0.18):
#     total_amount = sum(item['price'] * item['quantity'] for item in cart)
#     gst_amount = total_amount * gst_rate
#     final_amount = total_amount + gst_amount
#     return total_amount, gst_amount, final_amount

# def send_email(to_email, name, cart, total, gst, final_amount):
#     sender_email = "sneha.snehamayee@gmail.com"
#     sender_password = "ztkg kemb qpnm cgys"
    
#     subject = "Supermarket Bill Details"
#     items_details = "\n".join([f"{item['name']}: {item['quantity']}kg/unit @ Rs.{item['price']}" for item in cart])
#     message = (f"Subject: {subject}\n\n"
#                f"Hi {name},\n\n"
#                f"Here is your purchase summary:\n\n"
#                f"{items_details}\n\n"
#                f"Total Amount: Rs. {total:.2f}/-\n"
#                f"GST (18%): Rs. {gst:.2f}/-\n"
#                f"Final Amount: Rs. {final_amount:.2f}/-\n\n"
#                f"Thank you for shopping with us!")
    
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     s.starttls()
#     s.login(sender_email, sender_password)
#     s.sendmail(sender_email, to_email, message)
#     s.quit()
#     print("Email sent successfully!")

# def generate_bill():
#     data = fetch_supermarket_data()
#     if not data:
#         return
    
#     display_available_items(data)
    
#     name = input("Enter your name: ")
#     email = input("Enter your email: ")
    
#     cart = []
#     while True:
#         item_name = input("Enter item name (or 'done' to finish): ")
#         if item_name.lower() == 'done':
#             break
        
#         quantity = float(input("Enter quantity (kg or grams): "))
#         price = next((item['price'] for item in data if item['name'].lower() == item_name.lower()), None)
        
#         if price is None:
#             print("Item not found. Please try again.")
#             continue
        
#         cart.append({"name": item_name, "quantity": quantity, "price": price})
    
#     total, gst, final_amount = calculate_bill(cart)
#     bill_text = (f"\nName: {name}\n"
#                  f"\nItem Details:\n"
#                  + "\n".join([f"{item['name']}: {item['quantity']}kg/unit @ Rs.{item['price']}" for item in cart]) + "\n"
#                  f"\nTotal Amount: Rs. {total:.2f}/-\n"
#                  f"GST (18%): Rs. {gst:.2f}/-\n"
#                  f"Final Amount: Rs. {final_amount:.2f}/-")
    
#     choice = input("Do you want to send a mail or generate a bill? (mail/bill): ")
#     if choice.lower() == "mail":
#         send_email(email, name, cart, total, gst, final_amount)
#     else:
#         print("\nFinal Bill:")
#         print(bill_text)

# if __name__ == "__main__":
#     generate_bill()
