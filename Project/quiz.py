# #This program

# print("**********************************")
# print("----Quiz Game----")
# print("**********************************")
# print()
# print("Welcome")
# print()

# print("Are you ready??")
# q1 = ['kathmandu', 'snowman', 'muktinath', 'phewa tal', 'sherpa']

# print("Q1: What is the capital of kathmandu?")
# print("Options:\n1. Kathmandu\n2. Delhi\n3. Beijing\n4. Tokyo")
# userInput = input("Answer: ").lower()
# try:
#     if userInput in q1:
#         print("Wow, You guessed correct answer")
#     else:
#         print("Oops, thats not the one")
# except ValueError as e:
#     print("Invalid Input")
# print()
# print("Q2. What is the other name for the abominable snowman living in the Nepali mountains and, in general, in the Himalayas ranges?")
# print("Options:\n1. Sbowm\n2. Ooch Ka Ty\n3. Yeti\n4. Snowman") 
# userInput2 = input("Answer: ").lower()
# try:
#     if userInput2 in q1:
#         print("Wow, You guessed correct answer")
#     else:
#         print("Oops, thats not the one")
# except ValueError as e:
#     print(f"{e}")
# print()
# print("Q3. What is a famous pilgrimage site in Nepal Himalayas, both for Buddhist and Hindu pilgrims?")
# print("Options:\n1. Badrinath\n2. Sonamnath\n3. Amarnath\n4. Muktinath") 
# userInput3 = input("Answer: ").lower()
# try:
#     if userInput3 in q1:
#         print("Wow, You guessed correct answer")
#     else:
#         print("Oops, thats not the one")
# except ValueError as e:
#     print(f"{e}")
# print()
# print("Q4. What's the name of the people living in the valleys of Khumbu, Eastern Nepal, who provide most of the porters for trekkers?")
# print("Options:\n1. Sherpa\n2. Indra\n3. Magar\n4. Gurung") 
# userInput4 = input("Answer: ").lower()
# try:
#     if userInput4 in q1:
#         print("Wow, You guessed correct answer")
#     else:
#         print("Oops, thats not the one")
# except ValueError as e:
#     print(f"{e}")
# print()
# print("Q5. What is the name of the beautiful lake by which Pokhara lies?")
# print("Options:\n1. Sun Lake\n2. Naini Tal\n3. Himal Lake\n4. Phewa Tal") 
# userInput5 = input("Answer: ").lower()
# try:
#     if userInput5 in q1:
#         print("Wow, You guessed correct answer")
#     else:
#         print("Oops, thats not the one")
# except ValueError as e:
#     print(f"{e}")

# #q5.  What is the name of the beautiful lake by which Pokhara lies?
# # ["Sun Lake", "Naini Tal", "Himal Lake", "Phewa Tal"]


def ask_question(question, options, correct_answer):
    print(question)
    print("Options:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    user_input = input("Answer: ").lower()
    if user_input == correct_answer.lower():
        print("Wow, You guessed the correct answer!")
        return 1  # Return 1 for correct answer
    else:
        print("Oops, that's not the correct answer.")
        return 0  # Return 0 for incorrect answer

questions = {
    "Q1": ("What is the capital of Kathmandu?", ['Kathmandu', 'Delhi', 'Beijing', 'Tokyo'], 'Kathmandu'),
    "Q2": ("What is the other name for the abominable snowman in the Nepali mountains and Himalayas?", ['Sbowm', 'Ooch Ka Ty', 'Yeti', 'Snowman'], 'Yeti'),
    "Q3": ("What is a famous pilgrimage site in Nepal Himalayas, for both Buddhist and Hindu pilgrims?", ['Badrinath', 'Sonamnath', 'Amarnath', 'Muktinath'], 'Muktinath'),
    "Q4": ("What's the name of the people living in the valleys of Khumbu, Eastern Nepal, who provide most of the porters for trekkers?", ['Sherpa', 'Indra', 'Magar', 'Gurung'], 'Sherpa'),
    "Q5": ("What is the name of the beautiful lake by which Pokhara lies?", ['Sun Lake', 'Naini Tal', 'Himal Lake', 'Phewa Tal'], 'Phewa Tal')
}

print("Are you ready??")

correct_answers_count = 0

for key, (question, options, correct_answer) in questions.items():
    correct_answers_count += ask_question(f"{key}: {question}", options, correct_answer)
    print()

print(f"You got {correct_answers_count} out of {len(questions)} questions correct!")

