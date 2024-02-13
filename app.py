questions = (" 1. What is biggest technology company in South Korea? ",
             " 2. Which animal can be seen on the Porsche logo? ",
             " 3. Who is the first women to win a Nobel Prize? ",
             " 4. What is the most consumed manufactured drink in the world? ")
#options is a tuple which builds multiple options for each questions
options = (("A. Apple", "B. Samsung", "C. LG", "D. Lotte"),
           ("A. Lion", "B. Horse", "C. Jaguar", "D. Bull"),
           ("A. Donna Strickland", "B. Andrea Ghez", "C. Marie Curie", "D. Jennifer Doudna"),
           ("A. Tea", "B. Coffee", "C. Beer", "D. Orange Juice"))
guesses = []
question_num = 0 #inorder to print each questions in the tuple questions
answers = ("B", "B", "C", "A") #correct answers of the quiz.
score = 0 #to be able to track user's points which will be incremented by 1 a
# fter each loop.
for J in questions:# prints each questions j represents as the iteration value.
      print("----------------------------------")
      print(J)
      for i in options[question_num]:#this command gives different options for each questions i represents iteration value of options.
             print(i)
      guess = input("Enter A,B,C,D: ").upper()#we use upper,in case the user input answers in small letter.
      guesses.append(guess)#user's guess will be appended to the list guesses.
      if guess == answers[question_num]:#condition , if the user's guess equal to the actual answer user will get a point.
        score+=1
        print("Correct Answer")
      else:#if the user's guess not equal to the actual answer user will not  get a point and displays the correct answer.
         print("Incorrect Answer")
         print(f"{answers[question_num]}")

      question_num += 1#increments question number by 1 means automatically the next question will be displayed on the screen.

print("---------------------------------")
print("             RESULT  ")
print("---------------------------------")
print("CORRECT ANSWERS:")#correct answers of all the question will be displayed.
for i in answers:
    print(i)#prints each answers.

print("YOUR QUESSES:")#prints the answers we quessed.
for guess in guesses:
    print(guess)

score=score/len(questions)*100#points are converted to percentage
print("YOUR TOTAL PERCENTAGE IS", end=" ")
print(str(score))#we used str(score) , a string will not concatinate with int or float so that we converted the score to string.