class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0

    def next_question(self):
        question_to_be_asked = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q{self.question_number} : {question_to_be_asked.text} ? (True/False): ')
        self.check_answer(user_answer, question_to_be_asked.answer)


    def still_has_questions(self):
        # return self.question_number >= len(self.question_list)  -> Will do the same functionality as the code below
        if self.question_number >= len(self.question_list):
            return False
        else:
            return True


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('Answer is correct!!')
            self.user_score += 1
        else:
            print('Answer is incorrect')
        print(f'The correct answer is {correct_answer}')
        print(f'Your current score is: {self.user_score}/{self.question_number}')
