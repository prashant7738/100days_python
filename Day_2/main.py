import random
import variable

def lookup(lst):
    adjusted_lst = []
    for x in lst:
        if x == 11:
            adjusted_lst.append(1)
        else:
            adjusted_lst.append(x)
    return adjusted_lst

def end():
    print("Do you want to play again? Type 'y' or 'n'")
    while True:
        res = input().lower()
        if res == 'y':
            game()
        elif res == 'n':
            print("Thanks for playing. Goodbye!")
            break



def game():
    ucard = [random.choice(variable.card), random.choice(variable.card)]
    ccard = [random.choice(variable.card)]
    
    print(f"Your cards: {ucard}, current score: {sum(ucard)}")
    print(f"Computer's first card: {ccard[0]}")
    
    def play():
        if sum(ucard) == 21:
            print("JACKPOT!!! You win 😁. This is incredible Luck!!")

        res = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if res == 'y':
            ucard.append(random.choice(variable.card))
            if sum(ucard) < 21:
                print(f"Your cards: {ucard}, current score: {sum(ucard)}")
                play()
            else:
                temp = lookup(ucard)
                if sum(temp) < 21:
                    print(f"Your cards: {temp}, current score: {sum(temp)}")
                    play()
                elif sum(temp) ==21:
                    print("JACKPOT!!! You win 😁")
                else:
                    print(f"Your final card: {temp}, final score: {sum(temp)}")
                    print("You went over. You lose 😭")

        elif res == 'n':
            ccard.append(random.choice(variable.card))
            if sum(ucard) < sum(ccard):
                temp = lookup(ucard)
                if sum(ccard) > sum(temp):
                    print(f"Computer's final card: {ccard}, final score: {sum(ccard)}")
                    print("You went lower. You lose 😭")
                else:
                    print("You win 😁")
            elif sum(ucard) > sum(ccard):
                print(f"Computer's final card: {ccard}, final score: {sum(ccard)}")
                print("You win 😁")
            else:
                print(f"Computer's final card: {ccard}, final score: {sum(ccard)}")
                print("The game is a tie")

    play()
    end()

print(variable.intro)
game()

