import streamlit as st
from multiapp import MultiApp
from apps import home, data, univariate, bivariate, model # import app modules here
import streamlit.components.v1 as stc

#Title for the page
HTML_BANNER = """
<div style="background-color:#F63366;padding:10px;border-radius:10px">
<h1 style="color:white;text-align:center;">Financial Inclusion - East Africa</h1>
</div>
    """
stc.html(HTML_BANNER)

st.sidebar.image(
"https://www.cgap.org/sites/default/files/styles/blog_centered_800/public/inline-images/Villagers-Use-Mobile-Phone-in-Kenya.jpg", width=300)

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Dataset", data.app)
app.add_app("Unidimensional Analysis", univariate.app)
app.add_app("Multidimensional Analysis", bivariate.app)
app.add_app("Models", model.app)

# The main app
app.run()
