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
        starred = [f'* {x}' for x in correct_answers]
        joined = '\n'.join(starred)
        verb = "are" if len(correct_answers) > 1 else "is"
        st.error(f"Nope!\nThe correct answers {verb}:\n{joined}")
    st.markdown("[Audio](<https://otter.ai/s/CMqz0gzRQuaqysgNFQms9A?snpt=true>)")
