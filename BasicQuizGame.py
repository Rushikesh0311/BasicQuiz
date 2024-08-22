# List of quiz questions, options, and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["a) Paris", "b) London", "c) Berlin", "d) Madrid"],
        "answer": "a"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["a) 3", "b) 4", "c) 5", "d) 6"],
        "answer": "b"
    },
    {
        "question": "What is the boiling point of water?",
        "options": ["a) 50°C", "b) 100°C", "c) 150°C", "d) 200°C"],
        "answer": "b"
    }
]


# Function to display a question and get the user's answer
def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    
    answer = input("Your answer: ").lower()
    while answer not in ["a", "b", "c", "d"]:
        answer = input("Please enter a valid option (a, b, c, d): ").lower()
    
    if answer == question_data["answer"]:
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect. The correct answer was {question_data['answer']}.\n")
        return False

# Main function of the program run the quiz
def main():
    score = 0
    for question in quiz_questions:
        if ask_question(question):
            score += 1
    
    print(f"Quiz finished! Your final score is: {score}/{len(quiz_questions)}")

if __name__ == "__main__": # Entry point of the program
    main()
