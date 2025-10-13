import streamlit as st
#C:\Users\JML\AppData\Local\Programs\Python\Python312\python.exe -m streamlit run "C:\Users\JML\KI - Projekte\Spamfilter-Naive-Bayes\gui.py"


st.title("Spamfilter with Naive Bayes - ML")

input_text = st.text_input("Please enter a message in English please")

if st.button("Rating Message"):
    print("hallo")
    st.success("Die Nachricht ist kein Spam")


if st.button("Clear Message"):
    pass

st.write("A Project from [https://github.com/Juljano](%s)" % "https://github.com/Juljano")
