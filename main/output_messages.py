from abc import ABC, abstractmethod

class BaseOutputMessage(ABC):
    @abstractmethod
    def message():
        pass

class ListOfCommandsMessage(BaseOutputMessage):
    def message():
        print('List of available commands:')
        print(
            '\nadd_record name phone(only numbers) birthday(format: DD.MM.YYYY)\
            \ndelete_record name\
            \nadd name phone\
            \ndelete name phone\
            \nchange name old_phone new_phone\
            \nclose/exit\
            \nphone name\
            \ndays_to_birthday name\
            \nsearch arguments\n'
        )

class ContactAddedMessage(BaseOutputMessage):
    def message(name, phone):
        print(f'Contact with name {name} and phone {phone} was successfully added!')

class ContactDeletedMessage(BaseOutputMessage):
    def message(name):
        print(f'Contact with name {name} was successfully removed!')

class SearchMatchesMessage(BaseOutputMessage):
    def message(match_contacts):
        print(f'List of matches: {match_contacts}' if match_contacts else None)

class PhoneAddedMessage(BaseOutputMessage):
    def message(name, user_phone):
        print(f'The phone number {user_phone} was successfully added to contact {name}!')

class PhoneDeletedMessage(BaseOutputMessage):
    def message(name, user_phone):
        print(f'The phone number {user_phone} was successfully removed from contact {name}!')

class PhoneChangedMessage(BaseOutputMessage):
    def message(name, old_phone, new_phone):
        print(f'The phone number {old_phone} in contact {name} was successfully changed to {new_phone}')

class DaysToBirthdayMessage(BaseOutputMessage):
    def message(name, days):
        print(f'Days to {name}\' birthday: {days}')

class TypeErrorMessage(BaseOutputMessage):
    def message():
        print('You didn\'t put user\'s phone or name!')

class KeyErrorMessage(BaseOutputMessage):
    def message():
        print('Error!')

class ContactExistsErrorMessage(BaseOutputMessage):
    def message():
        print('This contact already exist!')

class ContactDoesNotExistErrorMessage(BaseOutputMessage):
    def message():
        print('This contact does not exist!')

class PhoneDoesNotExistErrorMessage(BaseOutputMessage):
    def message():
        print('The phone number that you\'re trying to change/delete does not exist!')

class PhoneExistsErrorMessage(BaseOutputMessage):
    def message():
        print('The phone number that you\'re trying to add already exist!')

class IndexErrorMessage(BaseOutputMessage):
    def message():
        print('This command does not exist!')

class ValueErrorMessage(BaseOutputMessage):
    def message():
        print('Put birthday in format DD.MM.YYYY')

class OnlyNumbersErrorMessage(BaseOutputMessage):
    def message():
        print('Phone number must include only numbers!')