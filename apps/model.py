import streamlit as st
import time
from apps.classifier import Classifier
from sklearn.preprocessing import LabelEncoder

def format_data(data):
    en = LabelEncoder()

    with st.empty():
        st.info("⏳ Compiling data...")

        temp = []
        result = []

        for item in data.values():
            if(isinstance(item, int)):
                temp.append(item)
            else:
                temp.append(en.fit_transform([item]))

        result.append(temp)

        print(result)

        return result

def app():

    # Load model
    model = Classifier()

    # Create data columns
    col1, col2 = st.beta_columns(2)

    with col1:
        countries = ['Kenya', 'Rwanda', 'Tanzania', 'Uganda']
        country = st.selectbox("Select country", countries)

        years = [2018, 2016, 2017]
        year = st.selectbox("Select Year", years)

        locations = ['Rural', 'Urban']
        location_type = (st.selectbox('Select Location', locations))

        cellphone_access = st.selectbox("Respondent has a cellphone?", ['Yes', 'No'])

        statuses = ['Married/Living together', 'Widowed', 'Single/Never Married',
                    'Divorced/Seperated', 'Dont know']

        marital_status = st.selectbox("Marital status", statuses)

        realtionships = ['Spouse', 'Head of Household', 'Other relative', 'Child', 'Parent',
                        'Other non-relatives']
        relationship_with_head = st.selectbox("Relationship with the household head", realtionships)

    with col2:
        gender_of_respondent = st.selectbox("Respondent's gender", ['Male', 'Female'])

        age_of_respondent = st.number_input("Enter respondent's age", min_value=1, max_value=100)

        levels = ['Secondary education', 'No formal education', 'Vocational/Specialised training', 'Primary education',
                    'Tertiary education', 'Other/Dont know/RTA']
        education_level = st.selectbox("Respondent's education level", levels)

        job_types = ['Self employed', 'Government Dependent',
                    'Formally employed Private', 'Informally employed',
                    'Formally employed Government', 'Farming and Fishing',
                    'Remittance Dependent', 'Other Income',
                    'Dont Know/Refuse to answer', 'No Income']
        job_type = st.selectbox("Respondent's job type", job_types)

        household_size = st.number_input("Respondent's household size", min_value=1)



    a,b,x,y,z = st.beta_columns(5)
    with a:
        pass
    with b:
        pass
    with x:
        if(st.button("Predict", help="Predict")):
            data = {
                    'country': country,
                    'year': year,
                    'location_type': location_type,
                    'cellphone_access': cellphone_access,
                    'household_size': household_size,
                    'age_of_respondent': age_of_respondent,
                    'gender_of_respondent': gender_of_respondent,
                    'relationship_with_head': relationship_with_head,
                    'marital_status': marital_status,
                    'education_level': education_level,
                    'job_type': job_type,
                    }
            print(data)
            result = format_data(data)
            res = model.predict(result)

            if(res[0] == 0):
                st.info("😃 User does not have a bank account")
                st.balloons()

            if(res[0] == 1):
                st.info("🙂 User likely has a bank account")

    with y:
        pass
    with z:
        pass



