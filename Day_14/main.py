import pandas as pd
data = pd.read_csv("002 weather-data.csv")

# #  TO FIND MEAN USING PYTHON 

# list_of_avg = data["temp"].to_list()
# avg = sum(list_of_avg) / len(list_of_avg)
# print(avg)

# #  OR
print(f"The mean value of temperature is {data['temp'].mean()}")

print(f"The highest value is {data['temp'].max()}")

print(f''' The highest temperature was in {data[data.temp == data.temp.max()].day.values[0]}''')





# #  TO CONVERT DATA FRAME INTO DICTIONARY

# convert dataframe to dictionary
data_dict = data.to_dict('records')
print(data_dict)


# data_dict = data_frame.to_dict()
# print(data_dict)