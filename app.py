import streamlit as st

# Streamlit Python´s framework

st.title("Customer registration")

name = st.text_input("First and last name")

address = st.text_input("Address")

birth_date = st.date_input("Birthday")

customer_reference = st.selectbox("Have you used our services before?", ["Yes, I am a customer already.","No, this is my first customer experience."])

register = st.button("Register")

st.subheader("Developed by Clovis de Melo")

st.subheader("Technologies: Python and Streamlit framework")

if register:
    with open("customers.csv", "a", encoding="utf8") as customers_database:
        customers_database.write(f"{name}, {address}, {birth_date}, {customer_reference}\n")
        st.success("Thanks for submitting your information!")