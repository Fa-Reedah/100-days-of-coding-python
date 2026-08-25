from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_bank = []

for i in question_data:
    question_form = Question(i["text"], i["answer"])
    # q1 = question_form.ques_tion
    # q2 = question_form.ans_wer
    Question_bank.append(question_form)

quiz = (QuizBrain(Question_bank))

while quiz.still_has_question() is True:
    answer = quiz.next_question()
    quiz.check_answer(answer)

print("You have completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.q_num}")






