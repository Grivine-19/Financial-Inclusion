import streamlit as st

def app():
    st.markdown('''
            ## **Overview**

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

    st.markdown('## About The Project')

    st.markdown('''
                ### Objective
                The objective of this project is to create a machine learning model
                to predict which individuals are most likely to have or use a bank account.
                The models and solutions developed can provide an indication of the state of
                financial inclusion in Kenya, Rwanda, Tanzania and Uganda, while providing
                insights into some of the key demographic factors that might drive individuals’
                financial outcomes.
                ''')

    st.markdown('''
                ### Tools used
                1. [Python 3](https://www.python.org/)

                2. [Plotly](https://plotly.com/)

                3. [Streamlit](https://streamlit.io/)

                4. [Scikit-learn](https://scikit-learn.org/)

                ''')


    st.markdown('''
                ### Approach

                1. Exploratory Data Analysis

                2. Data Cleaning

                3. Data Analysis

                4. Modeling

                5. Testing

                6. Publishing(Data App)
                ''')

    st.markdown('## The team')

    st.text('')

    col1, col2 = st.beta_columns(2)

    with col1:
        st.image('https://media-exp1.licdn.com/dms/image/C5603AQHNOz4SmNB0wQ/profile-displayphoto-shrink_800_800/0/1623075120453?e=1631750400&v=beta&t=acjp6w1cwM6xsesy9gnL42Suh6YxscGvM71YgmV7ZtA',
        width=300)

    with col2:
        st.markdown('''
                    ## Grivine Ochieng'

                    ### Data Scientist

                    [LinkedIn](https://www.linkedin.com/in/grivine/)

                    [GitHub](https://github.com/Grivine-19/)
                    ''')

    col3, col4 = st.beta_columns([1,2])

    with col3:
        st.markdown('''
                    ## Lewis Munyi

                    ### ML Engineer

                    [LinkedIn](https://www.linkedin.com/in/lewismunyi/)

                    [GitHub](https://github.com/lewis-munyi/)

                    ''')

    with col4:
        st.image('https://media-exp1.licdn.com/dms/image/C4D03AQEV458JYZO6cQ/profile-displayphoto-shrink_800_800/0/1568277850921?e=1627516800&v=beta&t=-2vvEjsVzKleODlw553YKMdDg7OVP6BPjj41vNbiDhg',
        width=300)