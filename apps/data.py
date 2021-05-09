import streamlit as st
import pandas as pd
import plotly.express as px  # Built in and simple to use
import plotly.graph_objects as go  # Low-level & a bit complex

@st.cache
def get_data(filename):
    finance_data = pd.read_csv(filename)
    
    return finance_data

def app():
    st.markdown(''' 
    #### **Description**

    The main dataset used for this project is from a Zindi Competition that merged data
    from different Finscope surveys ranging from 2016-2018. More information can be
    found here:

    * [FinAccess Kenya 2018](https://fsdkenya.org/publication/finaccess2019/)
    * [Finscope Rwanda 2016](http://www.statistics.gov.rw/publication/finscope-rwanda-2016)
    * [Finscope Tanzania 2017](http://www.fsdt.or.tz/finscope/)
    * [Finscope Uganda 2018](http://fsduganda.or.ug/finscope-2018-survey-report/)

    The table below Contains demographic information of approximately 25 thousand individuals
    across East Africa. The 25K records are those that we obtained after cleaning the 
    original dataset.
    ''')

    finance_data = get_data('data/inclusion.csv')

#Display an interactive  Plotly tabel of the dataset
    fig = go.Figure(data=[go.Table(columnwidth=[2,2,2,2,2,3,3],header=dict(values=list(finance_data[['country', 'bank_account',
    'cellphone_access', 'gender_of_respondent', 'age_of_respondent', 'marital_status', 'education_level', 'job_type']].columns),
    fill_color='#1f77b4',
    align=['left', 'center'], height=40, font=dict(color='white', size=15)),

    cells=dict(values=[finance_data.country, finance_data.bank_account, finance_data.cellphone_access,
    finance_data.gender_of_respondent, finance_data.age_of_respondent, finance_data.marital_status,
    finance_data.education_level, finance_data.job_type],
    fill_color='#8c564b',
    align='left'))
    ])

    fig.update_layout(margin=dict(l=5, r=5, b=10, t=10))
    st.write(fig)
