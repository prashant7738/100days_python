class QuizBrian:
    def __init__ (self, q_list):
        self.question_number =0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        user_ans = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False): ")
        correct_ans =self.question_list[self.question_number].answer
        self.check_answer(user_ans, correct_ans)
        print(f"Your current score is: {self.score}/{self.question_number+1}")
        self.question_number += 1
        print("\n")


    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def final_result(self):
        print("You've completed the quiz")
        print(f"Your final score is: {self.score}/{len(self.question_list)}")


    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower() or user_ans.lower()[0] == correct_ans.lower()[0]:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            print("The correct answer was: ", correct_ans)

        





   

    

