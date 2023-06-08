import pandas, csv


# csv_data = pandas.read_csv("Starting+Files+-+coffee-and-wifi/cafe-data.csv")
# print(csv_data)

# row = [{"Coffee Name": "Olawale Street Market", "Location": "Just testing", "Open": "8AM", "Close": "9AM", "Coffee": "x", "Wifi": "xx", "Power": "xxxx"}]
# df = pandas.DataFrame(row)
# # print(df)

# df.to_csv("Starting+Files+-+coffee-and-wifi/cafe-data.csv", mode = "a", header= False, index= False)
with open('Starting+Files+-+coffee-and-wifi/cafe-data.csv', newline='') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    
    list_of_rows = []
    for row in csv_data:
        list_of_rows.append(row)

for rows in list_of_rows:
    if list_of_rows[0] == rows:
        pass
    else:
        for col in rows:
            print(col)
