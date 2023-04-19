from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Lesson learned: Always put variables above everything
'''' _______________________[ ↓ Variables down here ↓ ]_______________________'''

question_bank = []
data = question_data['category']
category_choice = input('Choose a category [CS, Game, Geography]: ').lower()  #alway put input up top
total_quizz = int(input("How many quizz you want to play:  "))
print()

category = question_data['category'][category_choice]
Q = category[0]['question']
A = category[0]['correct_answer']
quiz = QuizBrain(question_bank, total_quizz)


'''' _____________________[ ↓ Code & Calling function ↓ ]_____________________'''

for question in category:
    each_question = question['question']
    new_question = Question(Q, A, )

    question_bank.append(each_question)

while quiz.still_has_question():
    p_answer = quiz.nextQuestion()  # contain input
    quiz.track_score(p_answer, A)
    quiz.still_has_question()  # print more questions
    print()

print("That all for today, go home dodge")