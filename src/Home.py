import streamlit as st

st.title("Flasher")

st.markdown("The spanish word is **pero**")
answer = st.text_input("English word")
submit = st.button("submit")
if submit:
    if answer == "but":
        st.info("Correct!!")
        st.balloons()
    else:
        st.error("Sorry!")
