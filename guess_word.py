from random import randint
print("Я загадал слово, попробуй угадать!: ")
bukvi = ["_", "_", "_", "_", "_"]
words = ["земле", "книга", "стена", "время", "птица"]
rand_word = words[randint(0, 4)]
while "_" in bukvi:
    print(bukvi)
    usr_input = input("Вводите только буквы!, только одну букву!: ")
    if not usr_input.isalpha():
        print("Я сказал только буквы!")
        continue
    if len(usr_input) > 1:
        continue
    for i in range(len(rand_word)):
        if usr_input == rand_word[i]:
            bukvi[i] = usr_input
print("Молодец! вы угадали слово! слово было -", rand_word)