import pandas as pd
import streamlit as st
import pickle as pkl
import os


# Hide the Streamlit sidebar menu
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

df = pd.read_csv("data/bank.csv")

st.title('Prediction for Bank Marketing Campaign')

# Sidebar for EDA and Dataset
st.sidebar.write("""
    [Exploratory Data Analysis](https://github.com/emekaefidi/Bank-Marketing-with-Machine-Learning/blob/master/Bank%20Marketing%20with%20Machine%20Learning.ipynb)
""")
st.sidebar.write("""
    [Dataset](https://archive.ics.uci.edu/static/public/222/bank+marketing.zip)
""")


st.write("This app is based on 16 inputs that predict wheather a customer will deposit or not? Using this app, a bank can identify specific customer segments; that will make deposits.")
st.write("Please use the following form to get started!")


# selecting job
st.subheader("Customer Job")
selected_job = st.selectbox("", df['job'].unique(), index = 3)
st.write("Selected Job : ", selected_job)
## Encode the job entered by user
### Declaring function for encoding
def encode_job(selected_item):
    dict_job = {'admin.':0, 'blue-collar':1, 'entrepreneur':2, 'housemaid':3, 'management':4, 'retired':5, 'self-employed':6, 'services':7, 'student':8, 'technician':9, 'unemployed':10, 'unknown':11}
    return dict_job.get(selected_item, 'No info available')
### Using function for encoding
selected_job = encode_job(selected_job)  

# selecting age
st.subheader("Customer Age")
selected_age = st.slider("", min_value = 18, max_value = 95, 
                         step = 1, value = 41)    # Slider does not tolerate dtype value mismatch df.age.max() was thus not used.
st.write("Selected Age : ", selected_age)


# selecting marital status
st.subheader("Customer Marital")
selected_marital = st.radio("", df['marital'].unique())
st.write("Selected Marital : ", selected_marital)
## Encode the marital entered by user
### Declaring function for encoding
def encode_marital(selected_item):
    dict_marital = {'divorced':0, 'married':1, 'single':2}
    return dict_marital.get(selected_item, 'No info available')
### Using function for encoding
selected_marital = encode_marital(selected_marital)  


# selecting education
st.subheader("Customer Education")
selected_education = st.radio("", df['education'].unique())
st.write("Selected Education : ", selected_education)
## Encode the education entered by user
### Declaring function for encoding
def encode_education(selected_item):
    dict_education = {'primary':0, 'secondary':1, 'tertiary':2, 'unknown':3}
    return dict_education.get(selected_item, 'No info available')
### Using function for encoding
selected_education = encode_education(selected_education)  

 # selecting default status
st.subheader("Customer Default Status")
selected_default = st.radio("", df['default'].unique()[::-1])
st.write("Selected Default Status : ", selected_default)
## Encode the default entered by user
### Declaring function for encoding
def encode_default(selected_item):
    dict_default = {'no':0, 'yes':1}
    return dict_default.get(selected_item, 'No info available')
### Using function for encoding
selected_default = encode_default(selected_default)  


# selecting balance
st.subheader("Customer Balance")
selected_balance = st.slider('', min_value = -6847,
          max_value = 81204, step = 1, value = int(df.balance.mean()))
st.write("Selected Customer Balance : ", selected_balance)      


# selecting housing status
st.subheader("Customer Housing Status")

selected_housing = st.radio("", df['housing'].unique(), 
                            index = 1, key = "1")
st.write("Housing Status : ", selected_housing)
## Encode the housing entered by user
### Declaring function for encoding
def encode_housing(selected_item):
    dict_housing= {'no':0, 'yes':1}
    return dict_housing.get(selected_item, 'No info available')
### Using function for encoding
selected_housing = encode_housing(selected_housing)  


# selecting loan status
st.subheader('Loan Status')
selected_loan = st.radio("", df['loan'].unique()[::-1], index = 1, key = "2")
st.write("Loan Status : ", selected_loan)
## Encode the loan entered by user
### Declaring function for encoding
def encode_loan(selected_item):
    dict_loan= {'no':0, 'yes':1}
    return dict_loan.get(selected_item, 'No info available')
### Using function for encoding
selected_loan = encode_loan(selected_loan)  


# selecting contact
# st.title("Customer Contact")
st.subheader("Customer Contact")

selected_contact = st.radio("", df['contact'].unique(), 
                            index = 1)
st.write("Contact Type : ", selected_contact)

## Encode the contact entered by user
### Declaring function for encoding
def encode_contact(selected_item):
    dict_contact= {'cellular':0, 'telephone':1, 'unknown':2}
    return dict_contact.get(selected_item, 'No info available')
### Using function for encoding
selected_contact = encode_contact(selected_contact)  

# selecting day
st.subheader('Day')
day_range = list(range(df['day'].min(), df['age'].max()))
selected_day = st.selectbox('Select Day:',(day_range), index = 19)
st.write('Selected Day : ', selected_day)

# selecting month
st.subheader('Last Contact Month of Customer')
selected_month = st.selectbox("", df['month'].unique(), 
                            index = 1)
st.write("Selected Month : ", selected_month)
## Encode the month entered by user
### Declaring function for encoding
def encode_month(selected_item):
    dict_month = {'apr':0, 'aug':1, 'dec':2, 'feb':3, 'jan':4, 'jul':5, 'jun':6, 'mar':7, 'may':8, 'nov':9, 'oct':10, 'sep':11}
    return dict_month.get(selected_item, 'No info available')
### Using function for encoding
selected_month = encode_month(selected_month)  


# selecting duration
st.subheader("Customer Duration")
selected_duration = st.slider('', min_value = 2,
                     max_value = 3881, step = 1, 
                     value = int(df.duration.mean()))
st.write("Duration : ", selected_duration)



# selecting campaign
st.subheader('Number of Contacts Peroformed in this Campaign')
campaign_range = list(range(df['campaign'].min(), df['campaign'].max()))
selected_campaign = st.selectbox('',(campaign_range), index = 0)
st.write('You selected : ', selected_campaign)


# selecting pdays
st.subheader('Number of Days Before the Customer was Contacted')
pdays_range = list(range(df['pdays'].min(), df['pdays'].max()))
selected_pdays = st.selectbox('',(pdays_range), index = 0)
st.write('You selected : ', selected_pdays)


# selecting previous
st.subheader('Number of Contacts Performed Before this Campaign')
previous_range = list(range(df['previous'].min(), df['previous'].max()))
selected_previous = st.selectbox('',(previous_range), index = 0)
st.write('You selected : ', selected_previous)


# selecting poutcome
st.subheader('Outcome of Previous Campaign') 
selected_poutcome = st.radio("", df['poutcome'].unique(), index = 0)
st.write("Selected poutcome : ", selected_poutcome)
## Encode the poutcome entered by user
### Declaring function for encoding
def encode_pout(selected_item):
    dict_pout = {'failure':0, 'other':1, 'success':2, 'unknown':3}
    return dict_pout.get(selected_item, 'No info available')
### Using function for encoding
selected_poutcome = encode_pout(selected_poutcome) 


# Adding Features
dur_pdays = ((selected_duration + selected_previous**0.15 - 
              (selected_contact**2)**0.0003 )**2)**0.25


contact_housing = (selected_housing)**(0.2) + (selected_campaign)**(0.35) + selected_contact**(0.2)


pickle_in = open("model/model.pkl","rb")
classifier = pkl.load(pickle_in)


prediction = classifier.predict([[selected_age, selected_marital, 
                                  selected_education, selected_balance,  
                                  selected_housing, selected_loan, 
                                  selected_day, selected_month, selected_poutcome, 
                                  selected_duration, 
                                  selected_campaign, selected_pdays, selected_contact, 
                                  dur_pdays, contact_housing, selected_job, selected_default]])




# Adding Predict Button
predict_button = st.button('Predict')
# st.write(predict_button)

if predict_button:
    if(prediction == 1):
        st.success('Eligble for Loan')
    else:
        st.success('Not Eligble for Loan')    

st.write('\n')
about = st.expander('More about app')
about.write("https://github.com/Varshitha-Neelapu/Bank/blob/main/README.md")
