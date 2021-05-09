from re import X
import streamlit as st
import plotly.express as px 
import plotly.graph_objects as go
from apps.data import get_data

finance_data = get_data('data/inclusion.csv')

def app():
    menu = ["Bank Account", "Residence", "Employment", "Education", "Phone Access", "Data Distribution"]
    choice=st.selectbox("Choose to view", menu)

    if choice == "Residence":
        t2 = px.histogram(finance_data, x="location_type", title="<b>Residence</b>",
        color_discrete_map={"Rural":"goldenrod", "Urban":"magenta"})
        st.write(t2)
        st.text("The distribution of rural and urban population is almost equal with"
        "the majority of people living in rural areas")

    elif choice == "Employment":
        t3 = px.histogram(finance_data, x="job_type", title="<b>Employment Types</b>",
        color_discrete_sequence=px.colors.qualitative.Vivid)
        st.write(t3)
        st.text("Majority of the population were mostly self employed"
        "and informally employed, or practicing farming and fishing")

    elif choice == "Education":
        t4 = px.histogram(finance_data, x="education_level", title="<b>Education Level</b>",
        color_discrete_sequence=px.colors.qualitative.Bold)
        st.write(t4)
        st.text("Majority of the population have attained primary level of education")
    
    elif choice == "Phone Access":
        t5 = px.histogram(finance_data, x="cellphone_access", title="<b>Mobile Phone Access</b>",
        color_discrete_map={"Yes":"red", "No":"green"})
        st.write(t5)
        st.text("Majority of the population have access to a mobile phone")

    elif choice == "Bank Account":
        t1 = px.histogram(finance_data, x="bank_account", title="<b>Bank Account Status</b>", color_discrete_map={
        "Yes": "goldenrod", "No": "red"})  # Challenge with explicit color mapping for histogram values
        st.write(t1)
        st.text("Most East African's do not have bank accounts")
    
    else:
        col1, col2 = st.beta_columns([1,3])
        with col1:
            options1 = ['gender_of_respondent', 'country', 'job_type',
            'education_level']
            x = st.selectbox("Choose x-axis value", options1)
            choice1 = x

            options2 = [None, 'bank_account','marital_status', 'cellphone_access']
            color = st.selectbox("Select hue",options2)
            
        with col2:
            fig = px.violin(finance_data, y="age_of_respondent", x=choice1, color=color,
            box=True, points="all", color_discrete_sequence=px.colors.qualitative.Dark2)
            st.write(fig)
        
