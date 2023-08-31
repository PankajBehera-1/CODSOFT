import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Answer the following questions to test your knowledge.")
        print("Let's begin!\n")

    def present_question(self, question):
        print(question["question"])
        for i, choice in enumerate(question["choices"], start=1):
            print(f"{i}. {choice}")
        user_answer = input("Your choice: ")
        return int(user_answer) - 1

    def evaluate_answer(self, user_answer, question):
        correct_answer = question["answer"]
        if user_answer == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print("Incorrect.")
            print(f"The correct answer is: {question['choices'][correct_answer]}\n")

    def display_final_results(self):
        print("Quiz completed!")
        print(f"Your final score is: {self.score} out of {len(self.questions)}")

    def play_again(self):
        choice = input("Do you want to play again? (yes/no): ")
        return choice.lower() == "yes"
    
    def display_final_results(self):
        print("\nQuiz completed!")
        print(f"Your final score is: {self.score} out of {len(self.questions)}")
        
        percentage = (self.score / len(self.questions)) * 100
        if percentage >= 70:
            print("Congratulations! You performed well.")
        else:
            print("You can do better. Keep practicing!")

def main():
    quiz_questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["Paris", "Berlin", "Rome", "Madrid"],
            "answer": 0,
        },
        {
            "question": "What is the largest planet in our solar system?",
            "choices": ["Mars", "Jupiter", "Venus", "Saturn"],
            "answer": 1,
        },
        {
            "question": "Which famous scientist developed the theory of relativity?",
            "choices": ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Galileo Galilei"],
            "answer": 1,
        },
        {
            "question": "What is the chemical symbol for gold?",
            "choices": ["Ag", "Hg", "Au", "Pb"],
            "answer": 2,
        },
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "choices": ["William Shakespeare", "Mark Twain", "Charles Dickens", "Jane Austen"],
            "answer": 0,
        },
        {
            "question": "What is the process by which plants make their own food?",
            "choices": ["Respiration", "Photosynthesis", "Fermentation", "Transpiration"],
            "answer": 1,
        },
        {
            "question": "Which planet is known as the 'Red Planet'?",
            "choices": ["Mars", "Jupiter", "Venus", "Saturn"],
            "answer": 0,
        },
    ]

    game = QuizGame(quiz_questions)
    game.welcome_message()

    while True:
        random.shuffle(quiz_questions)
        for question in quiz_questions:
            user_choice = game.present_question(question)
            game.evaluate_answer(user_choice, question)

        game.display_final_results()
        if not game.play_again():
            break
    


if __name__ == "__main__":
    main()
