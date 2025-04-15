import streamlit as st

st.title("Flasher")

answer = st.text_input("What is the English word for **Qué**?")
submit = st.button("submit")
if submit:
    correct_answers = ["who", "that"]
    user_answer = answer.lower().strip()
    if user_answer in correct_answers:
        st.success("Correct!!")
        st.balloons()
    else:
        st.error("Sorry!")
        st.markdown("The correct answers are")
        for ca in correct_answers:
            st.markdown(f"* {ca}")
    st.markdown("[Audio](<https://otter.ai/s/CMqz0gzRQuaqysgNFQms9A?snpt=true>)")
