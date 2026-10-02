import streamlit as st
from openai import OpenAI

client = OpenAI()

st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="📚",
    layout="centered"
)

st.title("📚 AI Study Buddy")
st.caption("Turn your notes into explanations, quizzes, and flashcards.")

# Sidebar
st.sidebar.header("Study Settings")

mode = st.sidebar.selectbox(
    "Choose a study mode:",
    [
        "💡 Explain a Concept",
        "🧠 Quiz Me",
        "🃏 Flashcards"
    ]
)

# Notes
st.subheader("1. Add your study notes")

notes = st.text_area(
    "Paste your notes below:",
    height=250,
    placeholder="Paste your class notes here..."
)

# Question
if mode == "💡 Explain a Concept":
    st.subheader("2. Ask a question")

    question = st.text_input(
        "What would you like explained?",
        placeholder="What is supervised learning?"
    )

elif mode == "🧠 Quiz Me":
    st.subheader("2. Choose a quiz topic")

    question = st.text_input(
        "What topic should I quiz you on?",
        placeholder="Machine learning"
    )

else:
    st.subheader("2. Choose a flashcard topic")

    question = st.text_input(
        "What topic should the flashcards cover?",
        placeholder="Supervised vs. unsupervised learning"
    )


# AI button
if st.button("✨ Generate", use_container_width=True):

    if not notes:
        st.warning("Please add some study notes first.")

    elif not question:
        st.warning("Please enter a topic or question.")

    else:

        if mode == "💡 Explain a Concept":

            instructions = """
You are an AI study assistant.

Answer the student's question using ONLY the study notes provided.

Explain the concept clearly and at a beginner-friendly level.
Use examples when helpful.

If the answer cannot be found in the notes, say:
"I don't know based on the provided notes."
"""

            user_input = f"""
Study notes:

{notes}

Student question:

{question}
"""

        elif mode == "🧠 Quiz Me":

            instructions = """
You are an AI study assistant helping a student study.

Using ONLY the provided study notes, create a short practice quiz
about the requested topic.

Create 5 questions.
Mix multiple-choice and short-answer questions.

Do NOT provide the answers immediately.
"""

            user_input = f"""
Study notes:

{notes}

Quiz topic:

{question}
"""

        else:

            instructions = """
You are an AI study assistant.

Using ONLY the provided study notes, create 5 useful flashcards
about the requested topic.

Format each flashcard like:

Card 1
Question: ...
Answer: ...

Keep the answers concise and useful for studying.
"""

            user_input = f"""
Study notes:

{notes}

Flashcard topic:

{question}
"""

        with st.spinner("AI is studying your notes..."):

            response = client.responses.create(
                model="gpt-5-mini",
                instructions=instructions,
                input=user_input
            )

        st.divider()

        if mode == "💡 Explain a Concept":
            st.subheader("💡 Explanation")

        elif mode == "🧠 Quiz Me":
            st.subheader("🧠 Practice Quiz")

        else:
            st.subheader("🃏 Flashcards")

        st.write(response.output_text)