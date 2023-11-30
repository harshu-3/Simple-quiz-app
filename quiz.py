class Question:
    def __init__(self, prompt, options, correct_option):
        self.prompt = prompt
        self.options = options
        self.correct_option = correct_option

    def display(self):
        print(self.prompt)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")
        print()

    def check_answer(self, user_answer):
        return user_answer == self.correct_option


def run_quiz(questions):
    score = 0
    for question in questions:
        question.display()
        user_answer = input("Your answer (enter the option number): ")
        
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if 1 <= user_answer <= len(question.options):
            if question.check_answer(user_answer):
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was {question.correct_option}.\n")
        else:
            print("Invalid input. Please enter a valid option.\n")

    print(f"You scored {score}/{len(questions)}.")


# Example Questions
question1 = Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 3)
question2 = Question("Which programming language is this quiz written in?", ["Java", "Python", "C++", "JavaScript"], 2)
question3 = Question("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], 2)

quiz_questions = [question1, question2, question3]

# Run the quiz
run_quiz(quiz_questions)
