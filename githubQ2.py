def reverse_list(input_list):
    reverse_list = []
    for i in range (len(input_list) -1,-1,-1):
        reverse_list.append(input_list[i])
    return reverse_list

old_list = [10,20,30,40,50]
reversed_result = reverse_list(old_list)
print("old list:",old_list)
print("Reversed List:",reversed_result)