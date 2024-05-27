import streamlit as st
from textblob import TextBlob
from streamlit_option_menu import option_menu
import base64


with st.sidebar:
    selected=option_menu(
    menu_title="Main Menu",
        options=['Home'],
        icons=['house'],
        styles={
            "container":{"background-color":"#7AA2E3"},
            "nav-link":{
                "font-size":"21px",
                "--hover-color":"#facf7d",
                "color":"317202A"
            },
            "nav-link-selected":{
                "background-color":"#fedc57"
            },
            "icon":{
                "font-size":"20px"
            },
        },
    )

if selected == 'Home':
    st.markdown("""
    <style>
    .big-font1{
    font-size:50px !important;
    color:#1693a7;
    text-align:center;
    font-weight:bold;
    
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="big-font1"> WELCOME TO THE SENTIMENT ANALYSIS SYSTEM </p>',unsafe_allow_html=True)
    file_=open("sent.png","rb")
    contents=file_.read()
    data_url=base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" width="700" image-align="center"  alt="Heart gif">',
        unsafe_allow_html=True, )

    st.markdown("""
    <style>
    . paragraph {
        font-size:20px !important;
        text-align: justify;
        }
    </style>
        """, unsafe_allow_html=True)

    st.markdown(' <p class="paragraph">TextBlob is a Python library used to perform NLP tasks like tokenization, POS-Tagging, Words inflection, Noun phrase extraction, lemmatization, N-grams, and sentiment Analysis. If you know about the state-of-the-art NLTK library, TextBlob has a few more features than it, such as Spelling correction, Creating a summary of a text, Translation, and language detection. It is an easy tool that covers all the necessary aspects of natural language processing. </p>',
    unsafe_allow_html=True)


  
    def get_sentiment(value):
        if value > 0:
            print(st.header("😃 Happy "))
        elif value < 0:
            return("😏 Sad")
        else:
            return("😐 Neutral")

    text = st.text_input("Enter Your Text and Press Enter to Run")

    blob = TextBlob(text)

    st.subheader("Emotion:")

    st.write(get_sentiment(blob.sentiment.polarity))

