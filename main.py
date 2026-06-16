import csv
from collections import Counter


class Library():
    def __init__(self, title, author, year, pages, genre, rating):
        self.title = title
        self.author = author
        self.year = int(year)
        self.pages = int(pages)
        self.genre = genre
        self.rating = float(rating)

    def __repr__(self):
        return f"{self.title} writen in {self.year} by {self.author} with a rating of: {self.rating}" 
    

def load_books(filename):
    books = []

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                books.append(
                    Library(
                        row["title"],
                        row["author"],
                        row["year"],
                        row["pages"],
                        row["genre"],
                        row["rating"],
                    )
                )

    except FileNotFoundError:
        print(f"Could not find '{filename}'.")
        return []

    return books


def average_rating(books):
    return sum(b.rating for b in books) / len(books) if books else 0

def longest_book(books):
     return max(books, key=lambda b:b.pages)

def shortest_book(books):
     return min(books, key=lambda b: b.pages)

def most_common_genre(books):
     genre = Counter(b.genre for b in books)
     return genre.most_common(1)[0]

def average_page_count(books):
     return sum(b.pages for b in books) / len(books)

def oldest_book(books):
     return min(books, key=lambda b: b.year)

def newest_book(books):
     return max(books, key=lambda b: b.year)


def main():
     books = load_books("books.csv")

     print(f"Total books: {len(books)}")
     print(f"Average rating: {average_rating(books)}")
     print(f"Average Pages: {average_page_count(books)}")
     print(f"Longest Book: {longest_book(books)}")
     print(f"Shortes book: {shortest_book(books)}")
     print(f"Most common genre: {most_common_genre(books)}")
     print(f"Oldest book: {oldest_book(books)}")
     print(f"Newest book: {newest_book(books)}")




if __name__ == "__main__": 
     main()