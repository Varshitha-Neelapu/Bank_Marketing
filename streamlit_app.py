import streamlit as st
from time import sleep
from navigation import make_sidebar
import mysql.connector

make_sidebar()

st.title("Bank Marketing")

st.write("Please log in to continue")

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bank_marketing"
)

# Create a cursor
cursor = connection.cursor()

# Streamlit app
def main():
    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        login()
    elif choice == "Register":
        register()

def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username and password:
            if authenticate_user(username, password):   
                st.session_state.logged_in = True
                st.success("Logged in successfully!")
                sleep(0.5)
                st.switch_page("pages/page1.py")   
            else:
                st.error("Invalid username or password")


    
def authenticate_user(username, password):
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    return True if result else False


        
def register():
    st.subheader("Register")
    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if st.button("Register"):
        if new_username and new_password and confirm_password:
            if new_password == confirm_password:
                if register_user(new_username, new_password):
                    st.success("Registration successful! Please login.")
                else:
                    st.error("Username already exists")
            else:
                st.error("Passwords do not match")

def register_user(username, password):
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    if result:
        return False
    else:
        insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(insert_query, (username, password))
        connection.commit()
        return True

if __name__ == "__main__":
    main()
# Close cursor and connection
cursor.close()
connection.close()