class QuizBrain:
    def __init__(self, question_list):
        self.q_list = question_list
        self.q_num = 0
        self.score = 0

    def still_has_question(self):
        return self.q_num < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.q_num].ques_tion
        self.q_num += 1
        answer = input(f"Q.{self.q_num}: {current_question} ('True/'False')?: ")
        return answer

    def check_answer(self, answer):
        # print(self.q_list[self.q_num-1].ans_wer.lower())
        # print(answer.lower())
        if answer.lower() == self.q_list[self.q_num-1].ans_wer.lower():
            self.score += 1
            print(f"You got it right!")
            #return True
        else:
            print(f"That's wrong!")
        print(f"The correct answer was: {self.q_list[self.q_num-1].ans_wer}")
        print(f"Your current score is: {self.score}/{self.q_num}")
        print("\n")