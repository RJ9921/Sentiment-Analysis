import streamlit as st
from textblob import TextBlob
from streamlit_option_menu import option_menu
import base64
from PIL import Image

with st.sidebar:
    selected=option_menu(
    menu_title="Main Menu",
        options=['Home','Prediction','Settings','About Us'],
        icons=['house','book','gear','envelope'],
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
    
    st.markdown('<p class="big-font1"> WELCOME TO THE EMOTION PREDICTION SYSTEM </p>',unsafe_allow_html=True)
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

if selected=='Prediction':
    st.markdown("""
    <style>
    .big-font1{
    font-size:50px !important;
    color:red;
    text-align:center;
    font-weight:bold;
    
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font1"> EMOTION PREDICTION SYSTEM </p>',unsafe_allow_html=True)
    image=Image.open('sent1.png')
    
    st.image(image,width=200,use_column_width=True)

    st.markdown("TextBlob is a Python library for processing textual data, offering a simple API to perform a variety of common natural language processing (NLP) tasks. Built on top of NLTK and the Pattern library, TextBlob simplifies complex language processing functionalities into an easy-to-use interface. It provides tools for part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more. TextBlob is particularly noted for its user-friendly syntax and seamless integration, allowing developers to efficiently handle tasks like tokenization, parsing, and linguistic analysis with minimal code. ")

    def get_sentiment(value):
        if value > 0:
            print(st.title("😃 Happy "))
        elif value < 0:
            print(st.title("😔 Sad "))
        else:
            print(st.title("😐 Neutral "))

    st.header('Enter Your Text and Press Enter to Run')
    text = st.text_input('Enter Text in Below Box')

    blob = TextBlob(text)

    st.subheader("Emotion:")


    sentiment_label = get_sentiment(blob.sentiment.polarity)
    if sentiment_label:
        st.header(sentiment_label)

if selected=='Settings':
    st.subheader('To Run This Project you need the Streamlit Environment and Required Libraries')
    st.subheader('Open Streamlit CMD and Type Command streamlit run app.py')
    st.subheader('A web application will get open in the default browser')


if selected=='About Us':
    st.subheader("A key feature of TextBlob is its simplicity and ease of use, making it highly accessible for both beginners and experienced developers working on natural language processing (NLP) projects. With its straightforward API, users can quickly perform complex NLP tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, translation, and text classification. TextBlob abstracts the complexities of underlying libraries like NLTK and Pattern, allowing for efficient text processing with minimal code. This user-friendly approach accelerates development and prototyping, making TextBlob an essential tool for rapid NLP application development and research.")

