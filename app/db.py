import streamlit as st
import mysql.connector

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
"""
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
    st.title("Login/Register App")
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
                   
                st.success("Logged in as {}".format(username))
                
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
    
from app import show_main_app

if __name__ == "__main__":
    main()
# Close cursor and connection
cursor.close()
connection.close()
"""