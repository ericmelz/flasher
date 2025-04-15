import streamlit as st
from data.flashcard_data import FlashcardData

if "flashcard_data" not in st.session_state:
    # Here we are entering the app for the first time.
    # We initialize the database and set the question state to NEW_QUESTION
    # The possible states are NEW_QUESTION, ANSWERING, and GUESSED
    # the state is NEW_QUESTION initially, and after the Next button is pressed.
    # the state is ANSWERING, while the question is being answered (e.g., right after NEW_QUESTION detected)
    # the state is GUESSED when the Submit button is pressed.
    st.session_state["flashcard_data"] = FlashcardData()
    st.session_state["fc_state"] = "NEW_QUESTION"
    st.session_state["fc"] = None

st.title("Flasher")

data = st.session_state["flashcard_data"]

if st.session_state["fc_state"] == "NEW_QUESTION":
    st.session_state["fc_state"] = "ANSWERING"
    fc = data.get_random_flashcard()
    st.session_state["fc"] = fc
    question = fc.question
    # TODO add this to data "What is the English word for **Qué**?"

human_answer = st.text_input(st.session_state["fc"].question)
print(f"*** after human_answer, {human_answer=}")

submit = st.button("submit")

if submit:
    print(f"*** submitted human_answer={human_answer}")
    st.session_state["fc_state"] = "GUESSED"


def reset():
    print("***resetting***")
    st.session_state["fc_state"] = "NEW_QUESTION"


if st.session_state["fc_state"] == "GUESSED":
    # Note here we use the saved flashcard from when we entered the ANSWERING state
    print(f"***{st.session_state['fc']=}")
    correct_answers = st.session_state['fc'].answers
    print(f"***{correct_answers=}")
    user_answer = human_answer.lower().strip()
    if user_answer in correct_answers:
        st.success("Correct!!")
        st.balloons()
    else:
        starred = [f'* {x}' for x in correct_answers]
        joined = '\n'.join(starred)
        verb = "are" if len(correct_answers) > 1 else "is"
        st.error(f"Nope!\nThe correct answers {verb}:\n{joined}")
    st.markdown("[Audio](<https://otter.ai/s/CMqz0gzRQuaqysgNFQms9A?snpt=true>)")

    st.markdown("new stuff")
    dummy_button = st.button("Dummy")
    next_button = st.button("Next", on_click=reset)
