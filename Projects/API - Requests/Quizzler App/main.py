from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_list = []
for question in question_data:
    #Get body and answer of question
    question_body = question["question"]
    question_answer = question["correct_answer"]

    #Create Question object with body and answer
    new_question = Question(question_body, question_answer)

    #Add question to question list
    question_list.append(new_question)


quiz = QuizBrain(question_list)  # Create quiz with question list
quiz_interface = QuizInterface(quiz) # Set up quiz user interface
