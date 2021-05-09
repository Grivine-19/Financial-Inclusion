import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from apps.data import get_data

finance_data = get_data('data/inclusion.csv')

def app():
    menu = ["Gender Vs Bank Account", "Education Vs Bank Account",
    "Marital Status Vs Bank Account", "Cellphone Access Vs Bank Account"]
    pick = st.selectbox("What comparisons do you want to make?", menu)

    if pick == "Gender Vs Bank Account":
        col1, col2 = st.beta_columns([1,3])

        with col1:
            options = ['bank_account', 'country']
            x = st.selectbox("Choose x-axis value", options)
            choice = x
            op = [None, 'bank_account']
            facet_col = st.selectbox("Split columns with...",op)
        with col2:
            t1 = px.histogram(finance_data, x=choice, color="gender_of_respondent",
            barmode='group', title="<b>Gender Vs Bank Account</b>",
            color_discrete_sequence=px.colors.qualitative.D3, facet_col=facet_col)
            st.write(t1)
            st.text("There are more males with bank accounts than females and more females without"
            "bank accounts than the males")

    elif pick == "Marital Status Vs Bank Account":
        col1, col2 = st.beta_columns([1, 3])

        with col1:
            options = ['bank_account', 'country']
            x = st.selectbox("Choose x-axis value", options)
            choice = x
            op = [None, 'marital_status']
            facet_col = st.selectbox("Split columns with...", op)
        with col2:
            t1 = px.histogram(finance_data, x=choice, color="marital_status",
            barmode='group', title="<b>Marital Status Vs Bank Account</b>",
            color_discrete_sequence=px.colors.qualitative.D3, facet_col=facet_col)
            st.write(t1)
            st.text("There are more married pple with bank accounts compared to the rest.")
    
    elif pick == "Cellphone Access Vs Bank Account":
        col1, col2 = st.beta_columns([1, 3])

        with col1:
            options = ['bank_account', 'country']
            x = st.selectbox("Choose x-axis value", options)
            choice = x
            op = [None, 'cellphone_access']
            facet_col = st.selectbox("Split columns with...", op)
        with col2:
            t1 = px.histogram(finance_data, x=choice, color="cellphone_access",
                              barmode='group', title="<b>Cellphone Access Vs Bank Account</b>",
                              color_discrete_sequence=px.colors.qualitative.D3, facet_col=facet_col)
            st.write(t1)
            st.text("Majority of the people with higher levels of education have access to a mobile phone.")

    else:
        col1, col2 = st.beta_columns([1, 3])

        with col1:
            options = ['bank_account', 'country']
            x = st.selectbox("Choose x-axis value", options)
            choice = x
            op = [None, 'education_level']
            facet_col = st.selectbox("Split columns with...", op)
        with col2:
            t1 = px.histogram(finance_data, x=choice, color="education_level",
                              barmode='group', title="<b>Education Vs Bank Account</b>",
                              color_discrete_sequence=px.colors.qualitative.D3, facet_col=facet_col)
            st.write(t1)
            st.text("A large number with tertiary and vocational education have bank accounts while a greater percentage of those with primary level of education do not have bank accounts.")
