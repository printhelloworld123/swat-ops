import streamlit as st

def create_text(text):
    return st.write(text)

def create_title(title):
    return st.title(title)

def create_question_text(question):
    return st.text_input(question)

# Options should be initialised in a list
def create_select_box(question, options):
    return st.selectbox(question, options)

# Options should be initialised in a list
def create_radio_buttons(question, options):
    return st.radio(question, options)

# Fields will map to keys, attributes will map to values of the JSON dictionary 
def create_json_view(text_display, fields, attributes):
    if st.button(text_display):
        return st.json({key:value for key, value in zip(fields,attributes)})
    
