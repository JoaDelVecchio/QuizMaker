class QuizBrain:
    def __init__(self,questionList):
        self.question_number = 0
        self.question_list = questionList
        self.score = 0

    def next_question(self):
        currentQuestion = self.question_list[self.question_number]
        self.question_number+=1
        userAnswer = input(f"Q{self.question_number}:{currentQuestion.text} True/False?\n")
        self.check_answer(userAnswer,currentQuestion.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self,userAnswer,correctAnswer):
        if correctAnswer.lower() == userAnswer.lower():
            self.score+=1
            print("You got it right")
        else:
            print("You got it wrong")
            
        print(f"The correct answer was {correctAnswer}")
        print(f"Current Score{self.score}/{self.question_number}")
        print("\n")
    