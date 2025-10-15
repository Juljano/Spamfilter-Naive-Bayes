import streamlit as st
#C:\Users\JML\AppData\Local\Programs\Python\Python312\python.exe -m streamlit run "C:\Users\JML\KI - Projekte\Spamfilter-Naive-Bayes\gui.py"

st.title("Spamfilter with Naive Bayes - ML")
input_text = st.text_input("Please enter a message in English.")

if st.button("Rating Message"):
    print(f"User-input: {input_text}")
    st.success("Die Nachricht ist kein Spam")


if st.button("Clear Message"):
    input_text = ""
    pass

st.write("A Project by [https://github.com/Juljano](%s)" % "https://github.com/Juljano")
