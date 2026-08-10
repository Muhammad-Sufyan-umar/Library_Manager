

from fileinput import filename

class Book:
	
	def __init__(self,book_id,title,author):
		self.book_id=book_id
		self.title=title
		self.author=author
		self.is_issued="Issued"
	
	def __str__(self):
			status=self.is_issued
			
			return f"ID: {self.book_id} |Author Name: {self.author} | Title: {self.title} |Status: {status}"
	
#-------------------------------------∆--------------_------

class Library:
	
	def __init__(self):
		self.books=[]
		

	
	#Add book--------_---------_-------->
	def add_book(self):
		book_id=input("enter book id: ")
		title=input("enter book title: ")
		author=input("enter author name: ")
		
		for book in self.books:
			if book.book_id==book_id:
				print("Book already  exists")
				return
		self.books.append(Book(book_id,title,author))
		print("Book added succesfully. \n")

	
	
	
	#View book--------_---------_-------->
	def view_books(self):
		if not self.books:
			print("No books available. \n")
			return
		print("-----Library------")
		for book in self.books:
			print(book)
	
	
	

	#Issue book--------_---------_-------->
	def issue_book(self):
		book_id=input("Enter book id:  ")
		for book in self.books:
			if book.book_id==book_id:
				if book.is_issued=="Issued":
					print("Book is already issued")
					return
				else:
					book.is_issued="Issued"
					print("Book successfully issued")
					return 
			else:
				print("Book not found \n")
				return


    #Return book--------_---------_-------->
	def return_book(self):
		book_id=input("Enter book id to return: ")
		for book in self.books:
			if book.book_id ==book_id:
				if book.is_issued != "Issued":
					print("Book already available")
					return
				else:
					book.is_issued = "Available"
					print("Book returned")
					return
			else:
				print("Book not found")

    #Save books to file--------_---------_-------->			
	def save_books_to_file(self, filename):
		with open(filename,"w") as f:
			for book in self.books:
				f.write(f"ID: {book.book_id}, Author: {book.author}, Title: {book.title}, Status: {book.is_issued}\n")
		
    #load books from file--------_---------_-------->


    
	def load_books_from_file(self, filename):
		try:
			with open(filename, "r") as f:
				for line in f:
					parts = line.strip().split(", ")
					book_id = parts[0].split(": ")[1]
					author = parts[1].split(": ")[1]
					title = parts[2].split(": ")[1]
					status = parts[3].split(": ")[1]
					book = Book(book_id, title, author)
					book.is_issued = status
					self.books.append(book)
		except FileNotFoundError:
			print("No saved books found. Starting with an empty library.")



	




def Main() -> None:
	library = Library()
	library.load_books_from_file("books.txt")

	while True:
		print("\n===== Library Management System =====")
		print("1. Add Book")
		print("2. View Books")
		print("3. Issue Book")
		print("4. Return Book")
		print("5. Exit")

		choice = input("Enter your choice: ")

		if choice == "1":
			library.add_book()

		elif choice == "2":
			library.view_books()

		elif choice == "3":
			library.issue_book()

		elif choice == "4":
			library.return_book()
		elif choice == "5":
			library.save_books_to_file("books.txt")
			print("Thank you for using Library Management System!")
			break
		else:
			print("Invalid choice. Please try again.")

Main()