import csv

# with open("002 weather-data.csv") as file:
#     data_list = [data.strip() for data in file.readlines()]
    

# It is easier using csv than that of manually reading file
with open("002 weather-data.csv") as file:
    data_file = csv.reader(file)
    temperature = []
    for row in data_file:
        if(row[1] != "temp"):
            temp = int(row[1])
            temperature.append(temp)

    print(temperature)



    # But it is also complicated so we use pandas library to make it easier