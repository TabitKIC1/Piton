phone_book = {}

def add_contact():
    name = input("введите имя: ")
    phone = input("введите номер телефона: ")
    phone_book[name] = phone
    print(f"контакт {name} добавлен .")

def delete_contact():
    name = input("введите имя контакта, который хотите удалить: ")
    if name in phone_book:
        del phone_book[name]
        print(f"контакт {name} успешно удален.")
    else:
        print(f"контакт {name} не найден.")

def edit_contact():
    name = input("введите имя которое хотите отредактировать: ")
    if name in phone_book:
        phone = input("введите новый номер : ")
        phone_book[name] = phone
        print(f"контакт {name} успешно изменен.")
    else:
        print(f"контакт {name} не найден.")

def print_contacts():
    if phone_book:
        print("список контактов:")
        for name, phone in phone_book.items():
            print(f"{name}: {phone}")
    else:
        print("список пуст.")

def main():
    while True:
        print("менюшка:")
        print("1. добавить контакт")
        print("2. редактировать контакт")
        print("3. удалить контакт")
        print("4. список")
        print("5. выйти")
        choice = input("ведите номер действия: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            print_contacts()
        elif choice == "5":
            break
        else:
            print("неверный ввод ведите ещё раз.")

if __name__ == '__main__':
    main()