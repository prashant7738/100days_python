from question_model import question
from data import question_data
from quiz_brain import QuizBrian

question_bank = []
for q in question_data:
    # question_bank.append(question(q['text'],q['answer']))

    quest= q['question']
    answer = q['correct_answer']

    question_bank.append(question(quest,answer))


# print(question_bank)

quiz = QuizBrian(question_bank)


while quiz.still_has_question():
    quiz.next_question()


quiz.final_result()

