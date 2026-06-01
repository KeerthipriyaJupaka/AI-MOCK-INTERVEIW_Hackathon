import streamlit as st
from pypdf import PdfReader
import pyttsx3

st.set_page_config(page_title="AI Mock Interview")

st.title("🎤 AI Mock Interview Platform")

# Resume Upload
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

job_description = st.text_area("Paste Job Description")

resume_text = ""

if resume_file:
    reader = PdfReader(resume_file)

    for page in reader.pages:
        txt = page.extract_text()
        if txt:
            resume_text += txt

    st.success("Resume Uploaded Successfully")

# Predefined Questions
questions = [
    "Tell me about yourself",
    "Explain Object Oriented Programming",
    "What is a SQL Join?",
    "Describe a challenging project",
    "Why should we hire you?"
]

if st.button("Start Interview"):
    st.session_state["current_question"] = 0

if "current_question" in st.session_state:

    q = questions[st.session_state["current_question"]]

    st.subheader("Interview Question")
    st.write(q)

    # Voice Output
    if st.button("🔊 Speak Question"):
        engine = pyttsx3.init()
        engine.say(q)
        engine.runAndWait()

    answer = st.text_area("Your Answer")

    if st.button("Submit Answer"):

        score = min(len(answer.split()), 100)

        st.write(f"Score: {score}/100")

        if st.session_state["current_question"] < len(questions) - 1:
            st.session_state["current_question"] += 1
            st.rerun()

        else:
            st.success("Interview Completed")
            st.balloons()

            total_score = 75

            st.subheader("Final Readiness Report")
            st.write(f"Readiness Score: {total_score}/100")
            st.write("Strengths: Communication, Problem Solving")
            st.write("Weaknesses: Technical Depth")
            st.write("Hiring Readiness: Average")