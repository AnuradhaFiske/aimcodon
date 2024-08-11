import streamlit as st
from datetime import datetime

# Title of the App
st.title("ServDish - Your Personal Chef at Home")

# Login Page
st.header("Login")
mobile_number = st.text_input("Mobile Number")
gmail_account = st.text_input("Gmail Account")
x_account = st.text_input("X Account (formerly Twitter)")
login_button = st.button("Login")

if login_button:
    st.success("Logged in successfully!")

    # User Profile Setup
    st.header("Profile Setup")
    name = st.text_input("Name")
    contact_number = st.text_input("Contact Number")
    address = st.text_area("Home Address")

    # Cuisine Selection
    st.header("Select Your Cuisine")
    cuisine_options = ["North Indian", "South Indian", "Gujarati", "Bengali", "Rajasthani", "Italian", "French", "American"]
    selected_cuisine = st.selectbox("Cuisine Type", cuisine_options)

    # Date and Time Selection
    st.header("Select Date and Time for the Service")
    order_date = st.date_input("Select Date", datetime.today())
    order_time = st.time_input("Select Time", datetime.now().time())

    # Beverage Selection
    st.header("Choose Your Beverages")
    beverage_options = ["Juices", "Smoothies", "Teas", "Coffees", "Soft Drinks"]
    selected_beverages = st.multiselect("Beverages", beverage_options)

    # Order Summary
    if st.button("Review Order"):
        st.header("Order Summary")
        st.write(f"*Name:* {name}")
        st.write(f"*Contact Number:* {contact_number}")
        st.write(f"*Address:* {address}")
        st.write(f"*Selected Cuisine:* {selected_cuisine}")
        st.write(f"*Selected Beverages:* {', '.join(selected_beverages)}")
        st.write(f"*Service Date:* {order_date}")
        st.write(f"*Service Time:* {order_time}")

        # Billing Page
        st.header("Billing Details")
        chef_cost = 300
        vegetable_cost = st.number_input("Enter Market Vegetable Cost (₹)", min_value=0, value=300)
        service_cost = 200
        other_ingredients_cost = 100
        delivery_cost = 100

        subtotal = chef_cost + vegetable_cost + service_cost + other_ingredients_cost + delivery_cost
        sgst = subtotal * 0.09  # 9% SGST
        cgst = subtotal * 0.09  # 9% CGST
        total_cost = subtotal + sgst + cgst

        st.write(f"*Chef Cost:* ₹{chef_cost}")
        st.write(f"*Vegetable Cost:* ₹{vegetable_cost}")
        st.write(f"*Service Cost:* ₹{service_cost}")
        st.write(f"*Other Ingredients Cost:* ₹{other_ingredients_cost}")
        st.write(f"*Delivery Cost:* ₹{delivery_cost}")
        st.write(f"*SGST (9%):* ₹{sgst:.2f}")
        st.write(f"*CGST (9%):* ₹{cgst:.2f}")
        st.write(f"*Total Amount:* ₹{total_cost:.2f}")

        if st.button("Confirm Order"):
            st.success(f"Order confirmed for {order_date} at {order_time}! A chef will arrive at your home as scheduled.")

            # Payment Mode Selection
            st.header("Payment Mode")
            payment_modes = ["Cash on Delivery (COD)", "Credit Card", "Debit Card", "Online Banking", "UPI"]
            selected_payment_mode = st.selectbox("Select Payment Mode", payment_modes)

            if st.button("Make Payment"):
                st.success(f"Payment method selected: {selected_payment_mode}. Your order is now complete!")

# Footer
st.write("---")
st.write("Thank you for using ServDish!")
