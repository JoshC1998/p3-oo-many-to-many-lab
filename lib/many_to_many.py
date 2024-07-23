class Author:
    def __init__(self, name: str):
        self.name = name
        self._contracts = []

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date: str, royalties: int):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)
    
class Book:
    def __init__(self, title: str):
        self.title = title
        self._contracts = []

    def __repr__(self):
        return f"Book(title={self.title})"

    def contracts(self):
        return self._contracts

    def authors(self):
        return [contract.author for contract in self._contracts]

class Contract:
    all = []

    def __init__(self, author, book, date: str, royalties: int):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        book._contracts.append(self)
        author._contracts.append(self)

    def __repr__(self):
        return f"Contract(author={self.author}, book={self.book}, date={self.date}, royalties={self.royalties})"

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]