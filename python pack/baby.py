from random import choice

questions = ["Why do we get hungry?: ", "Why do you watch football?: ",
             "How old are you?: "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why?: ").strip().lower()
print("Oh... Okay")
