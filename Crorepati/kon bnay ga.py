question1 = ["how many players are in cricket team.","11","12","14","10",1]
question2 = ["how is the famous footballer of all time on instagram.","ronaldo","messi","neymar","ramos",1]
question3 = ["the fastest bike is.","h2","zx","bmw","h2r",4]
question4 = ["current wwe champion.","brock","john cena","roman","seth",3]
question5 = ["strongest character in anime.","saitama","naruto","guko","sataro",3]
question6 = ["pakistan is in which contient.","europe","asia","australia","usa",2]

correct = [question1,question2,question3,question4,question5,question6]
levels = [1000,5000,15000,25000,50000,100000]

print("hello user are you ready.")
print("let's start the game.\n")

i =0
money = 0

for answer in correct: 
    print("========================================") 
    print(f"question for Rs.{levels[i]}")
    print(answer[0])
    print(f"a.{answer[1]}      b.{answer[2]}")
    print(f"c.{answer[3]}      d.{answer[4]}")

    reply = int(input("enter yours answer (1 to 4) and enter '0' to quit : "))
    if reply == 0:
        print("you have total won",money)
        break
    
    if reply == answer[-1]:
        print("correct asnwer")
        print(f"you have won RS.{levels[i]}\n")
        print()
        money += levels[i]
        i+=1
    else:
        print("wrong answer.")
        break
    
  

