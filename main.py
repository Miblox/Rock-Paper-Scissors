import random

itemss = ["камень", "ножницы", "бумага"]
print("Привет это игра камень ножницы бумага!")
round_game = 0
winner = 0
failedd = 0

for i in range(3):
    round_game += 1
    computer = random.choice(itemss)
    user_input = input("камень ножницы или бумага:  ").lower().strip()

    if user_input == "ножницы" and computer == "бумага":
        print(f"Ты выйграл! это {round_game} раунд")
        winner += 1

    elif user_input == "камень" and computer == "ножницы":
        print(f"Ты выйграл! это {round_game} раунд")
        winner += 1

    elif user_input == "бумага" and computer == "камень":
        print(f"Ты выйграл! это {round_game} раунд")
        winner += 1

    elif user_input == "ножницы" and computer == "камень":
        print(f"Ты проиграл! это {round_game} раунд")
        failedd += 1

    elif user_input == "бумага" and computer == "ножницы":
        print(f"Ты проиграл! это {round_game} раунд")
        failedd += 1

    elif user_input == "камень" and computer == "бумага":
        print(f"Ты проиграл! это {round_game} раунд")
        failedd += 1

    elif user_input == computer:
        print(f"Ничья! это {round_game} раунд")

    else:
        print("неверно! ты проиграл!")
        failedd += 1

if winner > failedd:
    print(f"Ты выйграл! твой резултат: Проиграл: {failedd}, Выйграно: {winner}")

elif winner == failedd:
    print(f"Ничья! твой резултат: Проиграл: {failedd}, Выйграно: {winner}")

else:
    print(f"Ты проиграл попробуй снова! твой резултат: Проиграл: {failedd}, Выйграно: {winner}")


input("\nНажмите Enter чтобы выйти... ")
