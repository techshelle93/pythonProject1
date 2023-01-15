import json
#import requests#
import streamlit as st
from PIL import Image
#from streamlit_lottie import st_lottie#


st. set_page_config(page_title="Jea's Webpage", page_icon=":tada:", layout="wide")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# ---- Load Assets ----
lottie_coding = load_lottiefile("lottiefiles/animate.json")
img_contact_form =Image.open("images/Project A.png")
img_contact_form_B =Image.open("images/Project B.png")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Jeannette's Python Webpage")
    st.title("I'm Looking for a Position within your Company :smile:")
    st.write("I am excited about learning Python and getting a Data Analyst job")
    st.write("[Learn More](averyjea.wixsite.com/avery-analytics)")

# ---- WHAT I DO----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I like to do")
        st.write("##")
        st.write(
            """ 
            I am excited to share that I have proficiencies in:
            - Microsoft Excel, Microsoft SQL Server, Power Bi and more. 
            
            - My major in Data Management Applications for  
                Healthcare will allow me to be in the healthcare field helping people behind the scenes
                and allow me to work with data. 
           
            - Helping people gives me a sense of accomplishment; and
                gives me a chance to make a difference in peoples lives indirectly through healthcare data
                 applications. 
             - I like data because it’s all around us such as all the products we have in our
                home, family and friends pictures we have stored, movies we have watched, our day to day budgeting; 
                these pieces of data tell a story about our lives."""
        )

        st.write("[LinkedIn Webpage](www.linkedin.com/in/jeannetteavery)")
#with right_column:#

#st_lottie(lottie_coding, height=300, key="coding")#

# ---- PROJECTS ----
    with  st.container():
        st.write("---")
        st.header("My Project")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
    with text_column:
        st.subheader("Dashboard Project")
        st.write("Dashboard executed with Tableau of Health Wearables data")
    with image_column:
        st.image(img_contact_form)
with st.container():

    st.header("School Project")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with text_column:
        st.subheader("Dashboard Project")
        st.write("Dashboard executed with Power BI of Health data")
    with image_column:
        st.image(img_contact_form_B)

# ---- Contact -----
with st.container():
    st.write("---")
    st.header("Contact Me")
    st.write("##")
    st.write("[Email me here](averyjea@gmail.com)")


