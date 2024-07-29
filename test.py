from address_book import AddressBook
from record import Record

def test(book: AddressBook):
# Створення нової адресної книги
    ##book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    john_record.add_birthday("27.07.2003")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    # for name, record in book.data.items():
    #     print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")


    #print(john)

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    #print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    #book.delete("Jane")

    #upcoming_birthdays = book.get_upcoming_birthdays()
    #print("Список привітань на цьому тижні:", upcoming_birthdays)

#test()