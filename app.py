import streamlit as st
import joblib

clf=joblib.load('loan.joblib')

st.title('LOAN APP')
g=st.number_input('Enter Gender 0:Male 1:Female')
m=st.number_input('Enter Marital Status 0:No 1:Yes')
ai=st.number_input('Enter Applicant Income')
la=st.number_input('Enter Loan Amount')

if st.button('PREDICT'):
    prediction=clf.predict([[g,m,ai,la]])
    if prediction=='Y':
        st.text('LOAN IS APPROVED')
    else:
        st.text('LOAN IS REJECTED')
