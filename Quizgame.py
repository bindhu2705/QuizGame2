import random

# Quiz questions and answers
questions = {
    "easy": {
        "What is the capital of France?": "Paris",
        "What is the largest planet in our solar system?": "Jupiter",
        "What is the smallest country in the world?": "Vatican City"
    },
    "medium": {
        "What is the chemical symbol for gold?": "Au",
        "What is the largest living species of lizard?": "Komodo dragon",
        "What is the deepest ocean trench?": "Mariana Trench"
    },
    "hard": {
        "What is the process by which water moves through a plant?": "Transpiration",
        "What is the largest known star in the universe?": "VY Canis Majoris",
        "What is the smallest bone in the human body?": "Stapes"
    }
}

def quiz_game():
    score = 0
    difficulty = input("Choose a difficulty level (easy, medium, hard): ")
    if difficulty not in ["easy", "medium", "hard"]:
        print("Invalid difficulty level. Defaulting to easy.")
        difficulty = "easy"

    question_list = list(questions[difficulty].items())
    random.shuffle(question_list)

    for question, answer in question_list:
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, that's incorrect. The correct answer is {answer}.")

    print(f"Your final score is {score} out of {len(question_list)}.")

if __name__ == "__main__":
    quiz_game()