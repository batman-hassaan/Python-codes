import time

question1 = ["how many players are in cricket team.","11","12","14","10",1]
question2 = ["how is the famous footballer of all time on instagram.","ronaldo","messi","neymar","ramos",1]
question3 = ["the fastest bike in the world is?.","h2","zx","bmw","h2r",4]
question4 = ["who is the current WWE champion.","brock","john cena","roman","seth",3]
question5 = ["who is the strongest character in anime.","saitama","naruto","guko","sataro",3]
question6 = ["Which continent is Pakistan in?.","europe","asia","australia","usa",2]
question7 = ["What is the capital of France?", "karachi", "Madrid", "Paris", "London", 3]
question8 = ["Who wrote 'To Kill a Mockingbird'?", " Charles Dickens", "Stephen King", "J.K. Rowling", "Harper Lee", 4]
question9 = ["What is the chemical symbol for gold?", "Fe", "Ag", "Au", "Cu", 3]
question10 = ["Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter", "Saturn", 2]
question11 = ["What is the tallest mammal?", "Kangaroo", "Elephant", "Horse", "Giraffe", 1]
question12 = ["Who painted the Mona Lisa? ", "Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo", 1]

correct = [question1,question2,question3,question4,question5,question6]
additional_questions = [question7, question8, question9, question10, question11, question12]
correct.extend(additional_questions)

level = [1000,5000,10000,20000,25000,50000,100000,150000,220000,360000,500000,1000000]

tmoney = 0
money = 0


print("Welcome to the quiz game\n")
time.sleep(1)
for i,answer in enumerate(correct):
    print("==================================")
    print(answer[0])
    print(f"a.{answer[1]}       b.{answer[2]}")
    print(f"c.{answer[3]}       d.{answer[4]}\n")
    reply = input("enter the correct answer (a,b,c,d) and 'Q' to Qiut : ").lower()
    if reply == 'q' :
        print(f"the total amount of money you won is :'{tmoney}'")
        break
    if reply == 'a' or reply == 'b' or reply == 'c' or reply == 'd':
        if reply == 'a':
            choose = 1
        elif reply == 'b':
            choose = 2
        elif reply == 'c':
            choose = 3
        elif reply == 'd':
            choose = 4

    if choose == answer[-1]:
        print("Congratuation!! your answer is correct")
        print(f"you have won {level[i]}")
        tmoney += level[i]
        # i+=1
        print("\n")
        if i ==  4:
            money = 20000
        elif i ==  7:
           money = 100000
           
    else:
        print("wrong answer, try next time.")  
        print(f"the money you have won is :{money}")
        break
    time.sleep(1)

