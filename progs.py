


def interface():
    print("добрый день ! Какую oперацию вы хотите произвести : \n 1 - запись данных \n 2 - вывод данных \n 3 - изменнение данных \n 4 - удаление данных \n 5 - Завершение программы ")
    command = int(input("Введите число "))
    while(True):
        match command:
            case 1:
                input_data()
                break
            case 2:
                print_data()
                break
            case 3:
                creat_data()
                break
            case 4:
                dell_data()
                break
            case 5: break
            case _: print("Неправильное число")    
    print("Программа завершена")
interface()
