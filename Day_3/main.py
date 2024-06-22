import data
import art
import random

def game():

    # This game is called higher or lower game in which we compare the followers of two individuals

    # first print the welcome logo
    print(art.logo)

    score = 0
    # Setting all data by shuffling it.
    random.shuffle(data.data)

    # Loop is taken till last of data dictionary so that we can compare two individuals.
    
    for n in range(len(data.data)-1):

        print(f"Compare A: {data.data[n]['name']}, a {data.data[n]['description']}, from {data.data[n]['country']}")
        print(art.vs)
        # print(f"Against B: {data.data[n+1]['name']}, a {data.data[n+1]['description']}, from {data.data[n+1]['country']}")

        print(f"Against B: {data.data[n+1]['name']}, a {data.data[n+1]['description']}, from {data.data[n+1]['country']}")

        res = input("Who has more followers? Type 'A' or 'B': \n ").lower()

        if(res == 'a' and data.data[n]['follower_count'] > data.data[n+1]['follower_count']):
            score += 1
            print(f"You're right! Current score: {score} \n")
        
        elif(res == 'b' and data.data[n+1]['follower_count'] > data.data[n]['follower_count']):
            score += 1
            print(f"You're right! Current score: {score} \n")
        else:
            break

    print(f"Sorry, that's wrong. Final score: {score} \n {art.cry}")
    
game()

