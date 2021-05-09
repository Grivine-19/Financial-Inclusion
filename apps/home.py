import streamlit as st

def app():
    col1, col2 = st.beta_columns(2)

    with col1:
        menu = ["About", "The Team"]
        choice=st.selectbox("What would you like to know?", menu)

        if choice == "The Team":
            st.markdown("""
            #### **Team Members:**
            [Jacklyne Betty](https: // www.linkedin.com/in/betty-jacklyne-03681535 / 'Jacklyne') - Professional Mentor

            [Grivine Ochieng](https: // www.linkedin.com/in/grivine / 'Grivine')

            [Lewis Munyi](https: // www.linkedin.com/in/lewismunyi / 'Lewis')
            """)
            
        else:
            st.markdown('''
            #### **Overview**

            Financial Inclusion remains one of the main obstacles to economic and human development
            in Africa. For example, across Kenya, Rwanda, Tanzania, and Uganda only 9.1 million
            adults (or 13.9% of the adult population) have access to or use a commercial bank
            account.

            Traditionally, access to bank accounts has been regarded as an indicator of
            financial inclusion. Despite the proliferation of mobile money in Africa,
            and the growth of innovative fintech solutions, banks still play a pivotal
            role in facilitating access to financial services. Access to bank accounts
            enable households to save and facilitate payments while also helping
            businesses build up their credit-worthiness and improve their access
            to other finance services. Therefore, access to bank accounts is an essential
            contributor to long-term economic growth.
            ''')

    with col2:
        menu = ["Objective", "Tools", "Approach"]
        choice = st.selectbox("Details on...", menu)

        if choice == "Tools":
            st.markdown(''' 
            * Python

            * Plotly

            * Streamlit
            ''')
            #statements here
        elif choice == "Approach":
            st.markdown(''' 
            #### **Steps**

            * Exploratory Data Analysis

            * Data Cleaning

            * Data Analysis

            * Modeling

            * Testing 

            * Publishing(Data App)
            ''')

        else:
            st.markdown(''' 
            #### **Objective**

            The objective of this project is to create a machine learning model to predict
            which individuals are most likely to have or use a bank account. The models and
            solutions developed can provide an indication of the state of financial inclusion
            in Kenya, Rwanda, Tanzania and Uganda, while providing insights into some of the
            key demographic factors that might drive individuals’ financial outcomes.
            ''')
