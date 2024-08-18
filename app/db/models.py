from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    total_copies = Column(Integer)
    issued_copies = Column(Integer, default=0)

    # Relationship with Inventory (many-to-many)
    inventories = relationship("Inventory", back_populates="book")

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    borrowed_books_count = Column(Integer, default=0)

    # Relationship with Inventory (many-to-many)
    inventories = relationship("Inventory", back_populates="student")

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    student_id = Column(Integer, ForeignKey("students.id"))

    # Relationships
    book = relationship("Book", back_populates="inventories")
    student = relationship("Student", back_populates="inventories")
