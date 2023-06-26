from collections import UserDict
from collections.abc import Iterator
from datetime import datetime
from errors import *
from output_messages import *

class AddressBook(UserDict):
    def add_record(self, name: str, phone: str, birthday: str | None = None) -> str:
        if name in self.data:
            raise ContactExistsError
        else:
            self.data[name] = Record(name, phone, birthday)
            return ContactAddedMessage.message(name, phone)

    def delete_record(self, name: str) -> str:
        if name not in self.data:
            raise ContactDoesNotExistError
        else:
            self.data.pop(name)
            return PhoneDeletedMessage.message(name)

    def search(self, arguments) -> str:
        match_contacts = []
        for name, contact in self.data.items():
            if arguments in name:
                match_contacts.append(name)
                continue
            for phone in contact.phones:
                if arguments in phone.value:
                    match_contacts.append(name)
                    break
        return SearchMatchesMessage.message(match_contacts)


class Record:
    def __init__(self, name: str, phone: str, birthday: str | None) -> None:
        self.name = Name(name)
        self.phones = [Phone(phone)]
        self.birthday = Birthday(birthday)

    def add(self, user_phone: str) -> str:
        if self.get_phone(user_phone):
            raise PhoneExistsError
        self.phones.append(Phone(user_phone))
        return PhoneAddedMessage.message(self.name.value, user_phone)

    def delete(self, user_phone: str) -> str:
        phone_in = self.get_phone(user_phone)
        if not phone_in:
            raise PhoneDoesNotExistError
        self.phones.remove(phone_in)
        return PhoneDeletedMessage.message(self.name.value, user_phone)

    def change(self, old_phone: str, new_phone: str) -> str:
        phone_in = self.get_phone(old_phone)
        if not phone_in:
            raise PhoneDoesNotExistError
        phone_in.value = new_phone
        return PhoneChangedMessage.message(self.name.value, old_phone, new_phone)

    def get_phone(self, user_phone) -> str | bool:
        for phone in self.phones:
            if user_phone == phone.value:
                return phone
        return False

    def days_to_birthday(self) -> str:
        if self.birthday.value is None:
            return None
        today = datetime.today()
        birthday = self.birthday.value.replace(year=today.year)
        if birthday < today:
            birthday = self.birthday.value.replace(year=today.year + 1)
        days = (birthday - today).days
        return DaysToBirthdayMessage.message(self.name.value, days)


class Field:
    def __init__(self, value) -> None:
        self.__value = None
        self.value = value


class Name(Field):
    def __init__(self, value) -> None:
        super().__init__(value)


class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if not value.isdigit():
            raise OnlyNumbersError
        self.__value = value


class Birthday(Field):
    def __init__(self, value) -> None:
        super().__init__(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value is not None:
            value = datetime.strptime(value, '%d.%m.%Y')
        self.__value = value
