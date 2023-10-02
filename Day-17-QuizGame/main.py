from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

QuestionBank = []

for q in question_data:
    q_text = q['text']
    q_answer = q['answer']
    question = Question(q_text,q_answer)
    QuestionBank.append(question)


quiz = QuizBrain(QuestionBank)

while quiz.still_has_questions():
    quiz.next_question()
    print('\n')   # Will Print a new Line

print('You have reached the end of Quiz!!')
print(f'Your final score is: {quiz.user_score}/{quiz.question_number}')