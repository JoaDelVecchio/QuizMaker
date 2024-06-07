from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for tuple in question_data:
    question = Question(tuple["text"],tuple["answer"])
    question_bank.append(question)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
  quiz.next_question()
  
  
print(f"You have completed the quiz...Score: {quiz.score}/{quiz.question_number}")




