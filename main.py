import csv
from collections import Counter

class Library():
    def __init__(self, title, author, year, pages, genre, rating):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.genre = genre
        self.rating = rating

    def __repr__(self):
        return f"{self.title} writen in {self.year} by {self.author} with a rating of: {self.rating}" 
    

def load_books(filename):
        books = []
        with open(filename, 'r') as books:
            reader = csv.DictReader(books)
            for row in reader:
                 book = Library(
                      row["title"],
                      row["author"],
                      row["year"],
                      row["pages"],
                      row["genre"],
                      row["rating"]
                 )
                 books.append(book)
        return books

def books_ammount(books):
     return len(books)

def average_rating(books):
     return float(sum(b.rating for b in books) / len(books))

def longest_book(books):
     return max(b.pages for b in books)

def shortest_book(books):
     return min(b.pages for b in books)

def most_common_genre(books):
     genre = Counter(b.genre for b in books)
     return genre.most_common(1)[0]

def average_page_count(books):
     return sum(b.pages for b in books) / len(books)

def oldest_book(books):
     return min(b.year for b in books)

def newest_book(books):
     return min(b.year for b in books)


def main():
     books = load_books("books.csv")

     print(f"Total books: {books_ammount(books)}")
     print(f"Average rating: {average_rating(books)}")
     print(f"Average Pages: {average_page_count}")
     print(f"Longest Book: {longest_book}")
     print(f"Shortes book: {shortest_book}")
     print(f"Most common genre: {most_common_genre}")
     print(f"Oldest book: {oldest_book}")
     print(f"Newest book: {newest_book}")




if __name__ == "__main__": 
     main()