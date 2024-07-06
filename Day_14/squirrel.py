import pandas as pd

data_of_squirel = pd.read_csv("squirrel_census.csv")
# print(data_of_squirel['Primary Fur Color'][3])
# print(len(data_of_squirel))

Gray = 0 
Cinnamon = 0
Black = 0
others = 0

for _ in range(len(data_of_squirel)):
    if(data_of_squirel['Primary Fur Color'][_] == "Gray"):
        Gray +=1

    elif(data_of_squirel['Primary Fur Color'][_] == "Cinnamon"):
        Cinnamon += 1

    elif(data_of_squirel['Primary Fur Color'][_] == "Black"):
        Black += 1
    
    else:
        others +=1


# print(others)

new_dict = {
    "Color" : ["Gray" , "Cinnamon" , "Black"],
    "Count" : [Gray , Cinnamon , Black]

}




new_frame = pd.DataFrame(new_dict)
# print(new_frame)

new_frame.to_csv("new.csv")