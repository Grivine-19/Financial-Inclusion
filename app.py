import streamlit as st
from multiapp import MultiApp
from apps import home, data, univariate, bivariate, model # import app modules here
import streamlit.components.v1 as stc

#Title for the page
HTML_BANNER = """
<div style="background-color:#f5b60a;padding:10px;border-radius:10px">
<h1 style="color:white;text-align:center;">Financial Inclusion;East Africa</h1>
</div>
    """
stc.html(HTML_BANNER)

st.sidebar.image(
"https://images.unsplash.com/photo-1567427017947-545c5f8d16ad?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=695&q=80", width=300)

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Dataset", data.app)
app.add_app("Unidimensional Analysis", univariate.app)
app.add_app("Multidimensional Analysis", bivariate.app)
app.add_app("Models", model.app)

# The main app
app.run()
