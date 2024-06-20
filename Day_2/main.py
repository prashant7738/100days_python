import random
import variable

print(variable.into)

def game():
    ucard = [random.choice(variable.card), random.choice(variable.card)]
    ccard = [random.choice(variable.card)]
    
    print(f"Your cards: {ucard}, current score: {sum(ucard)}")
    print(f"Computer's first card: {ccard[0]}")
    def play():
        res = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if res == 'y':
            ucard.append(random.choice(variable.card))
            if (sum(ucard) < 21):
                print(f"Your cards: {ucard}, current score: {sum(ucard)}")
                play()
                
            else:
                print(f"Your final card: {ucard}, final score: {sum(ucard)}")
                print("You went over. You lose 😭")

        elif res == 'n':
            ccard.append(random.choice(variable.card))
            if(sum(ucard)<sum(ccard)):
                print(f"Computer's final card: {ccard}, final score: {sum(ccard)}")
                print("You went lower. You lose 😭")
            
            elif(sum(ucard)>sum(ccard)):
                print(f"Computer's final card: {ccard}, final score: {sum(ccard)}")
                print("You win 😁")

            else:
                print(f"Computer's final card: {ccard}, final score: {sum(ccard)}")
                print("The game is a tie")

            

    play()
        
game()

