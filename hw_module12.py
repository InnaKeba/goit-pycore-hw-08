import pickle

class AddressBook:
    """
    Клас для зберігання списку контактів.
    """
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        if isinstance(contact, dict):
            self.contacts.append(contact)
            
    def get_contacts(self):
        return self.contacts

    def show_contacts(self):
        if not self.contacts:
            print("Адресна книга порожня.")
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact['name']} | Email: {contact['email']} | Телефон: {contact['phone']} | Обраний: {contact['favorite']}")

def save_data(book, filename="addressbook.pkl"):
    """
    Зберігає AddressBook у файл за допомогою pickle. Якщо файл не вдається зберегти, виводить повідомлення про помилку.
    """
    try:
        with open(filename, "wb") as f:
            pickle.dump(book, f)
        print("Дані успішно збережено.")
    except Exception as e:
        print(f"Помилка при збереженні: {e}")

def load_data(filename="addressbook.pkl"):
    """
    Завантажує AddressBook з файлу, або створює нову книгу, якщо файл не знайдено.
    """
    try:
        with open(filename, "rb") as f:
            print("Дані завантажено.")
            return pickle.load(f)
    except FileNotFoundError:
        print("Файл не знайдено. Створено нову адресну книгу.")
        return AddressBook()
    except Exception as e:
        print(f"Помилка при завантаженні: {e}")
        return AddressBook()

def main():
     # Завантаження адресної книги при запуску
    book = load_data() 

    print("\nАдресна книга:")
    book.show_contacts()

    # Додавання нового контакту
    new_contact = {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False
    }
    book.add_contact(new_contact)

    print("\nПісля додавання нового контакту:")
    book.show_contacts()

    # Збереження адресної книги перед виходом
    save_data(book)

if __name__ == "__main__":
    main()