immutable_var = (1, 2, 3, "sport", "top", True)
print(immutable_var)
# immutable_var[0] = 5 - операция выводится с ошибкой, т.к. нельзя изменить элемент кортежа
mutable_list = ["sport", 1, 2, 3, True, "top"]
print(mutable_list)
mutable_list[4] = 65
print(mutable_list)
mutable_list.append("apple")
print(mutable_list)
mutable_list.extend(["exit", 8])
print(mutable_list)
mutable_list.remove("sport")
print(mutable_list)
print("exit" in mutable_list) # для полноты понимания урока
print("top" not in mutable_list) # для полноты понимания урока
print("home" not in mutable_list) # для полноты понимания урока
print(mutable_list[::-1])