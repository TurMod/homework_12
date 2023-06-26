class ContactExistsError(Exception):
    ...


class ContactDoesNotExistError(Exception):
    ...


class PhoneExistsError(Exception):
    ...


class PhoneDoesNotExistError(Exception):
    ...


class OnlyNumbersError(Exception):
    ...


class AddressBookIsEmptyError(Exception):
    ...
