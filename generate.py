import os
import time
import random
from termcolor import colored
import sqlite3  # Импортируем библиотеку sqlite3

# Функция для очистки консоли
def clear_console():
    os.system('clear')  # Очистка для Linux/Mac
    # Для Windows используйте os.system('cls')

# Функция для отображения экрана загрузки с рандомным прогресс-баром
def loading_screen():
    clear_console()
    print("Загрузка... [", end='', flush=True)  # Начало прогресс-бара
    for _ in range(20):
        time.sleep(random.uniform(0.1, 0.5))  # Рандомная задержка от 0.1 до 1.0 секунд
        print("█", end='', flush=True)  # Отображение символа "█" без переноса строки
    print("]")  # Завершение прогресс-бара с закрывающей скобкой

# Вызываем функцию отображения экрана загрузки
loading_screen()
clear_console()

text = colored("BOT CODE CREATOR", "red")
print(f'\n{text}\n')
text = colored("v1.1", "yellow")
print(f'\n{text}')
text = colored("Made By t.me/Autoritetion", "yellow")
print(f'{text}\n')

loggined = False  # Инициализируем флаг, который будет указывать, вошел ли пользователь

def start():
    text = colored("Enter password>>> ", "blue")
    user_password = input(f'{text}')
    
    # Подключаемся к базе данных SQLite3
    db_connection = sqlite3.connect("psdb.db")  # Замените на путь к вашей базе данных
    
    if db_connection is not None:
        cursor = db_connection.cursor()
        
        # Выполняем SQL-запрос для поиска пароля
        cursor.execute("SELECT password FROM pas WHERE password = ?", (user_password,))
        
        # Получаем результат запроса
        result = cursor.fetchone()
        
        if result:
            text = colored("Successfully!", "green")
            print(text)
            global loggined
            loggined = True
        else:
            text = colored("Wrong password", "red")
            print(text)
            start()
        
        # Закрываем соединение с базой данных SQLite3
        cursor.close()
        db_connection.close()
    else:
        print("Unable to connect to the database.")

def main():
    start()
    
    if loggined == True:
        def log():
            text = colored("1.Create new code\n2.Info\n3.Exit", "red")
            print(f'\n{text}')
            text = colored(">>> ", "blue")
            nb = int(input(text))
            # dashboard
            if nb == 1:
                clear_console()
                text = colored("1.Generate code\n2.Codes\n3.Exit", "red")
                print(f"\n{text}")
                text = colored(">>> ", "blue")
                nbt = int(input(text))
            elif nb == 2:
                text = colored("This code can help you create code for Telegram bot", "yellow")
                print(f'\n{text}')
                log()
            elif nb == 3:
                clear_console()
                exit(-1)
        log()
    else:
        start()

main()
