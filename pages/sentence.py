import streamlit as st

def capitalize_sentence(sentence):
    return sentence.capitalize()

def uppercase_sentence(sentence):
    return sentence.upper()

def lowercase_sentence(sentence):
    return sentence.lower()

def reverse_sentence(sentence):
    return sentence[::-1]

def pig_latin_sentence(sentence):
    words = sentence.split()
    pig_latin_words = []
    for word in words:
        if word[0] in "aeiou":
            pig_latin_words.append(word + "yay")
        else:
            pig_latin_words.append(word[1:] + word[0] + "ay")
    return " ".join(pig_latin_words)


st.title("Sentence Transformer")
sentence = st.text_input("Enter a sentence:")
selected_transformation= st.radio("Select transformation", ["Capitalize", "Uppercase", "Lowercase", "Reverse", "Pig latin"])

transorm_button = st.button("Transform")
if transorm_button:
    if selected_transformation == "Capitalize":
        st.write(capitalize_sentence(sentence))
    elif selected_transformation == "Uppercase":
        st.write(uppercase_sentence(sentence))
    elif selected_transformation == "Lowercase":
        st.write(lowercase_sentence(sentence))
    elif selected_transformation == "Reverse":
        st.write(reverse_sentence(sentence))
    elif selected_transformation == "Pig latin":
        st.write(pig_latin_sentence(sentence))
    else:
        st.write("Please select a transformation")