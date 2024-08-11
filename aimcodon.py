import streamlit as st
import stripe
import os

# Set your Stripe API keys
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
YOUR_STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')

# Dummy data for available chefs
chefs = [
    {'id': 1, 'name': 'Chef Alice', 'price': 5000},  # Price in cents
    {'id': 2, 'name': 'Chef Bob', 'price': 6000}
]

def main():
    st.title("Personal Chef Booking App")

    # Display available chefs
    st.header("Available Chefs")
    for chef in chefs:
        st.subheader(chef['name'])
        st.write(f"Price: ${chef['price'] / 100:.2f}")
        if st.button(f"Book {chef['name']}", key=chef['id']):
            book_chef(chef)

def book_chef(chef):
    st.session_state['selected_chef'] = chef
    st.session_state['booking'] = True

def checkout():
    if 'booking' not in st.session_state:
        st.write("Please select a chef to book.")
        return

    chef = st.session_state['selected_chef']
    
    st.header(f"Checkout for {chef['name']}")
    st.write(f"Amount: ${chef['price'] / 100:.2f}")

    with st.form("payment_form"):
        card_number = st.text_input("Card Number")
        exp_month = st.number_input("Expiry Month", min_value=1, max_value=12, format="%d")
        exp_year = st.number_input("Expiry Year", min_value=2023, format="%d")
        cvc = st.text_input("CVC")
        submit_button = st.form_submit_button("Pay")

        if submit_button:
            # Payment logic here (Stripe integration)
            try:
                token = create_stripe_token(card_number, exp_month, exp_year, cvc)
                charge = stripe.Charge.create(
                    amount=chef['price'],
                    currency='usd',
                    source=token,
                    description=f"Payment for {chef['name']}"
                )
                st.success("Payment successful!")
            except stripe.error.CardError as e:
                st.error(f"Payment failed: {e.user_message}")

def create_stripe_token(card_number, exp_month, exp_year, cvc):
    token = stripe.Token.create(
        card={
            "number": card_number,
            "exp_month": exp_month,
            "exp_year": exp_year,
            "cvc": cvc,
        },
    )
    return token.id

if __name__ == "__main__":
    st.set_page_config(page_title="Personal Chef App", layout="wide")
    if 'booking' in st.session_state and st.session_state['booking']:
        checkout()
    else:
        main()




   
    
  
   
   
   
       
       
            

   
            


