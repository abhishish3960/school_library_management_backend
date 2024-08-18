import sys
import os

# Add the 'app' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


from app.db.session import SessionLocal, engine
from app.db.models import Book, Student, Inventory

def populate_data():
    session = SessionLocal()
    # Adding books
    books = [
        Book(title="The Great Gatsby", author="F. Scott Fitzgerald", total_copies=10, issued_copies=2),
        Book(title="To Kill a Mockingbird", author="Harper Lee", total_copies=8, issued_copies=4),
        Book(title="1984", author="George Orwell", total_copies=12, issued_copies=6),
        Book(title="Moby Dick", author="Herman Melville", total_copies=5, issued_copies=1),
        Book(title="Pride and Prejudice", author="Jane Austen", total_copies=7, issued_copies=3),
    ]
    session.add_all(books)

    # Adding students
    students = [
        Student(name="John Doe", email="john.doe@example.com", borrowed_books_count=2),
        Student(name="Jane Smith", email="jane.smith@example.com", borrowed_books_count=1),
        Student(name="Alice Johnson", email="alice.johnson@example.com", borrowed_books_count=3),
        Student(name="Bob Brown", email="bob.brown@example.com", borrowed_books_count=0),
        Student(name="Emily Davis", email="emily.davis@example.com", borrowed_books_count=1),
    ]
    session.add_all(students)

    session.commit()

    # Adding inventory records
    inventories = [
        Inventory(book_id=1, student_id=1),
        Inventory(book_id=2, student_id=1),
        Inventory(book_id=3, student_id=2),
        Inventory(book_id=4, student_id=3),
        Inventory(book_id=5, student_id=3),
        Inventory(book_id=3, student_id=3),
    ]
    session.add_all(inventories)

    session.commit()
    session.close()


if __name__ == "__main__":
    populate_data()
    print("Dummy data populated successfully.")
