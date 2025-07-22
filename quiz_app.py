import json

def load_questions(file_path="questions.json"):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Error loading questions: {e}")
        return []

def ask_question(index, question_data):
    q = question_data["question"]
    options = question_data["options"]

    print(f"\nQ{index + 1}: {q}")
    for key, val in options.items():
        print(f"  {key}. {val}")

    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in options:
            return answer
        else:
            print("⚠️ Invalid choice. Please enter A, B, C, or D.")

def run_quiz():
    questions = load_questions()
    if not questions:
        print("No questions to display.")
        return

    score = 0
    for i, question in enumerate(questions):
        user_answer = ask_question(i, question)
        correct_answer = question["answer"]

        if user_answer == correct_answer:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong. Correct answer was: {correct_answer}")

    total = len(questions)
    percentage = (score / total) * 100
    print("\n=== Quiz Finished ===")
    print(f"Score: {score} / {total}")
    print(f"Percentage: {percentage:.1f}%")

    if percentage == 100:
        print("🎉 Perfect score!")
    elif percentage >= 70:
        print("👍 Great job!")
    else:
        print("📘 Keep practicing!")

if __name__ == "__main__":
    print("=== Python Quiz App ===")
    run_quiz()
