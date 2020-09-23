from question import Question

question_prompts = [
    "What is your name?\n(a) Sir Lancelot of Camelot\n(b) Sir Robin\n(c) Sir Galahad\n\n",
    "What is your quest?\n(a) Burn the village\n(b) Prune the hedges\n(c) To seek the Holy Grail\n\n",
    "What is your favorite color?\n(a) Green\n(b) Blue \n(c) Yellow\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)
