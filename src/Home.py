import streamlit as st

st.title("Flasher")

st.markdown("<https://otter.ai/s/kR-WbeUUT7asz52Hwv0DNQ?snpt=true>")

st.markdown("The spanish word is **pero**")
answer = st.text_input("English word")
submit = st.button("submit")
if submit:
    if answer == "but":
        st.success("Correct!!")
        st.balloons()
    else:
        st.error("Sorry!")
        st.markdown("<https://otter.ai/s/kR-WbeUUT7asz52Hwv0DNQ?snpt=true>")

