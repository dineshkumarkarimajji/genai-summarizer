from transformers import pipeline

# Load GPT2 for text generation
generator = pipeline("text-generation", model="gpt2")

def generate_questions(text):
    prompt = f"Generate 3 logical or comprehension questions based on this:\n{text[:1000]}"
    generated = generator(prompt, max_length=200, num_return_sequences=1)
    output = generated[0]['generated_text']

    # Extract 3 questions from the generated text
    lines = [line.strip() for line in output.split('\n') if line.strip()]
    questions = [line for line in lines if '?' in line]

    return questions[:3]  # Return only first 3 questions

def evaluate_answer(user_answer, expected_answer):
    if user_answer.strip().lower() in expected_answer.strip().lower():
        return "✅ Correct!"
    else:
        return f"❌ Incorrect! Suggested answer: {expected_answer}"
