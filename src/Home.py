import streamlit as st
from src.data.flashcard_data import FlashcardData

# Configure the page with an appropriate icon and title
st.set_page_config(
    page_title="Flasher - Flashcard App",
    page_icon="⚡", # Lightning bolt - symbolizes flash/flashcards
    layout="centered",
    initial_sidebar_state="collapsed"
)

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

st.title("⚡ Flasher")

data = st.session_state["flashcard_data"]

if st.session_state["fc_state"] == "NEW_QUESTION":
    st.session_state["fc_state"] = "ANSWERING"
    tags = {"section": [5]}
    fc = data.get_random_flashcard(tags)
    # This is useful while developing / testing data
    # fc = data.get_last_flashcard(tags)
    st.session_state["fc"] = fc
    question = fc.question

human_answer = st.text_input(st.session_state["fc"].question)

submit = st.button("submit")

if submit:
    st.session_state["fc_state"] = "GUESSED"


def reset():
    st.session_state["fc_state"] = "NEW_QUESTION"


if st.session_state["fc_state"] == "GUESSED":
    # Note here we use the saved flashcard from when we entered the ANSWERING state
    correct_answers = [a.lower() for a in st.session_state['fc'].answers]
    user_answer = human_answer.lower().strip()
    if user_answer in correct_answers:
        st.success("Correct!!")
        st.balloons()
    else:
        if len(correct_answers) > 1:
            starred = [f'* {x}' for x in correct_answers]
            answer_display = '\n' + '\n'.join(starred)
        else:
            answer_display = f'**{correct_answers[0]}**'
        verb = "are" if len(correct_answers) > 1 else "is"
        s = "s" if len(correct_answers) > 1 else ""
        st.error(f"Nope!\nThe correct answer{s} {verb}: {answer_display}")
    if st.session_state['fc'].audio_url is not None:
        audio_url = st.session_state['fc'].audio_url
        st.markdown(f"[Audio]({audio_url})")

    next_button = st.button("Next", on_click=reset)
