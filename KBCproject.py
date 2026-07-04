# Create a program capable of displaying questions to the user like KBC
# Use list data type to display questions and their answers
# Display the final amount the person is taking home after playing the game

questions = [
    ["What is the capital of Nepal?", "A. Kathmandu", "B. Dhaka", "C. Male", "D. Thimphu", "A", 30000],
    ["What is the capital of Bangladesh?", "A. Kathmandu", "B. Dhaka", "C. Male", "D. Thimphu", "B", 40000],
    ["What is the capital of Maldives?", "A. Kathmandu", "B. Dhaka", "C. Male", "D. Thimphu", "C", 50000],
    ["What is the capital of Bhutan?", "A. Kathmandu", "B. Dhaka", "C. Male", "D. Thimphu", "D", 60000]
]

amount = 0

print("========= Welcome to KBC Quiz =========")

for question in questions:
    print("\n" + question[0])
    print(question[1])
    print(question[2])
    print(question[3])
    print(question[4])

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == question[5]:
        amount = question[6]
        print("Correct Answer!")
        print(f"You have won Rs. {amount}")
    else:
        print("Sorry, Wrong Answer!")
        print(f"The correct answer was {question[5]}")
        break

print("\n========= Game Over =========")
print(f"You are taking home Rs. {amount}")