from fields import *
import pickle


def main():

    try:
        with open('data.bin', 'rb') as fh:
            addressbook = pickle.load(fh)
    except FileNotFoundError:
        addressbook = AddressBook()

    def input_error(func):
        ListOfCommandsMessage.message()
        while True:
            try:
                result = func()
                if result == 'break':
                    break
            except TypeError:
                TypeErrorMessage.message()
            except (UnboundLocalError, KeyError):
                KeyErrorMessage.message()
            except ContactExistsError:
                ContactExistsErrorMessage.message()
            except ContactDoesNotExistError:
                ContactDoesNotExistErrorMessage.message()
            except PhoneDoesNotExistError:
                PhoneDoesNotExistErrorMessage.message()
            except PhoneExistsError:
                PhoneExistsErrorMessage.message()
            except (AttributeError, IndexError):
                IndexErrorMessage.message()
            except ValueError:
                ValueErrorMessage.message()
            except OnlyNumbersError:
                OnlyNumbersErrorMessage.message()

        with open('data.bin', 'wb') as fh:
            pickle.dump(addressbook, fh)

    @input_error
    def main_handler():
        while True:
            command, * \
                data = input('Write command: ').lower().strip().split(' ', 1)
            if data:
                data = data[0].split(' ')
            else:
                if command in ['close', 'exit']:
                    return 'break'
            if command in ['add_record', 'delete_record', 'search']:
                changes = getattr(addressbook, command)
                result = changes(*data)
            elif command == 'show_all':
                result = addressbook.iterator()
            else:
                if data[0] not in addressbook.data:
                    raise ContactDoesNotExistError
                elif command == 'phone':
                    result = [
                        i.value for i in addressbook.data.get(data[0]).phones]
                else:
                    changes = getattr(addressbook.data.get(data[0]), command)
                    result = changes(*data[1:])

            if result == 'break':
                return 'break'

if '__main__' == __name__:
    main()
