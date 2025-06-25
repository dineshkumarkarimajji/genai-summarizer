import streamlit as st
from utils import extract_text_from_file
from summarizer import generate_summary
from question_answering import ask_question 
from challenge_mode import generate_questions, evaluate_answer


st.set_page_config(page_title="GenAI Summarizer", layout="centered")
st.title("📄 GenAI Smart Research Summarizer")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF or TXT document", type=["pdf", "txt"])

# When file is uploaded
if uploaded_file:
    st.success("✅ File uploaded successfully!")
    
    # Extract text
    with st.spinner("Extracting text..."):
        document_text = extract_text_from_file(uploaded_file)

    # Show word count
    st.info(f"Document contains {len(document_text.split())} words.")

    # Generate summary
    st.subheader("📌 Summary (≤ 150 words)")
    with st.spinner("Generating summary..."):
        summary = generate_summary(document_text)
        st.success("✅ Summary generated")
        st.write(summary)


 


# Interaction Mode: Ask Anything
st.subheader("💬 Ask Anything Based on the Document")

user_question = st.text_input("Ask a question:")

if st.button("Get Answer") and user_question:
    with st.spinner("Searching for an answer..."):
        answer = ask_question(document_text, user_question)
        st.success("✅ Answer found")
        st.markdown(f"**Answer:** {answer}")

# Challenge Mode: Generate Questions

# Divider
st.markdown("---")

# Challenge Me Mode
st.subheader("🎯 Challenge Me: Test Your Understanding")

if st.button("Generate Questions"):
    with st.spinner("Creating challenge questions..."):
        st.session_state.questions = generate_questions(document_text)
        st.success("🧠 Questions generated!")

# Display and answer questions
if "questions" in st.session_state:
    user_answers = []

    for i, q in enumerate(st.session_state.questions):
        st.markdown(f"**Q{i+1}: {q}**")
        ans = st.text_input(f"Your Answer:", key=f"answer_{i}")
        user_answers.append(ans)

    if st.button("Submit Answers"):
        st.subheader("🧾 Evaluation Results")
        for i, user_ans in enumerate(user_answers):
            expected = "Check document manually"  # Placeholder
            evaluation = evaluate_answer(user_ans, expected)
            st.markdown(f"**Q{i+1} Evaluation:** {evaluation}")
