class LibraryUser:
    def __init__(self, id: int, name: str, address: str, email: str):
        self._id = id
        self._name = name
        self._address = address
        self._email = email
        self._books = []

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def books(self):
        return self._books

    def add_book(self, _book):
        self._books.append(_book)

    def remove_book(self, _book):
        self._books.remove(_book)

    
    def print(self):
        print("Name: " + self.name)
        print("Address: " + self.address)
        print("Email: " + self.email)