import pickle
from address_book import AddressBook

class FileStorage():
    '''Class for file storage handler base on pickle'''
    def __init__(self, filename: str = "addressbook.pkl"):
        self.filename = filename

    def save_data(self, book):
        '''Save object to file'''
        with open(self.filename, "wb") as fh:
            pickle.dump(book, fh)

    def load_data(self):
        '''Read object from file and deserialize'''
        try:
            with open(self.filename, "rb") as fh:
                return pickle.load(fh)
        except FileNotFoundError:
            return AddressBook()
