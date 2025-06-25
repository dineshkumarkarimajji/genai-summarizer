from transformers import pipeline

# Load Hugging Face QA model
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def ask_question(document_text, user_question):
    # Limit context size to first 3000 characters
    context = document_text[:3000]

    # Ask the model
    result = qa_pipeline(question=user_question, context=context)

    return result["answer"]
