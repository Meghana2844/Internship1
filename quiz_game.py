print('Quiz on Python Programming Language')
#function for checking correct answer
def check(guess,ans):
    if guess==ans:
        return True
    else:
        return False
#main function for the quiz
def quiz_game(questions,options,ans):
    score=0
    ques_num=0
    for question in range(len(questions)):
        print("*************************")
        print("Question Number", question + 1)
        print(questions[question])
        for i in options[ques_num]:
            print(i)
        guess=input('Enter Your Answer(A/B/C/D):').upper()
#checking whether the user input is correct or not

        is_correct=check(guess,answers[ques_num])
        if is_correct:
            print('CORRECT ANSWER :)')
            score+=1
        else:
            print("INCORRECT ANSWER :(")
            print(f'The Correct Answer is {answers[ques_num]}')
        ques_num+=1
#giving results based on the users answers
    print("*********RESULTS**********")   
    print(f"YOUR SCORE IS {score}/{len(questions)} ")
#questions for users
questions=("What does the 'len' function in Python determine?",
           "How do you insert an item at a specific index in a list?",
           "What keyword is used to define a function in Python?",
           "Which method is used to remove the first item from a list that has a specific value?",
           "What is the output of: print(8 // 3)?"
           )
#options for the questions
options=(("A.Data type", "B.Length of an object", "C.Maximum value", "D.Memory size"),
         ("A.append()", "B.insert()", "C.add()", "D.put()"),
         ("A.function", "B.def", "C.lambda", "D.func"),
         ("A.remove()", "B.delete()", "C.pop()", "D.discard()"),
         ("A.2.67", "B.2", "C.3", "D.2.0"))
#answers to the questions
answers=("B","B","B","A","B")
#run the quiz
quiz_game(questions,options,answers)