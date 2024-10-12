
name_list = ["Giorgi", "Ali", "Elene", "Andria", "Mariam", "Merabi", "Vano", "Anano", "Nata", "Lika"]

filtered_list = []

for i in range(len(name_list)):
    if name_list[i][0] != 'A':
        filtered_list.append(name_list[i])

print(filtered_list)
    
    # print(name_list[i])