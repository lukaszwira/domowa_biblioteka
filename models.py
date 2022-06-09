import json

class Books:
    def __init__(self):
        try:
            with open("./library.json", "r") as f:
                self.books = json.load(f)
        except FileNotFoundError:
            self.books = []
            
    def all(self):
        return self.books

    def get(self, id):
        for book in self.books:
            if book['id'] == id:
                return book
        return None

    def create(self, data):
        if 'csrf_token' in data:
            data.pop('csrf_token')
        data['id'] = self.books[-1]['id'] + 1 
        self.books.append(data)

    def save_all(self):
        with open("./library.json", "w") as f:
            json.dump(self.books, f)

    def update(self, id, data):
        if 'csrf_token' in data:
            data.pop('csrf_token')
        for idx, book in enumerate(self.books):
            if book['id'] == id:
                data['id'] = id
                self.books[idx] = data
                break

        self.save_all()
    
    def delete(self, id):
        book = self.get(id)
        if book:
            self.books.remove(book)
            self.save_all()
            return True
        return False


books = Books()