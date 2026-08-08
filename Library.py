class Book:
	
	def __init__(self,book_id,author,title):
		self.book_id=book_id
		self.title=title
		self.author=author
		self.is_issued=False
	
	def __str__(self):
			status="Issued" if self.is_issued else "Available"
			
			return f"ID: {self.book_id} |Name: {self.title} | Author: {self.author} |Status: {status}"
	
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
				if book.is_issued:
					print("book is already issued")
					return
				else:
					book.is_issued=True
					print("book sucussfully issued")
					return 
			else:
				print("Book not found \n")
				return


    #Return book--------_---------_-------->
	def return_book(self):
		book_id=input("Enter book id to return")
		for book in self.books:
			if book.book_id ==book_id:
				if not book.is_issued:
					print("Book already available")
				else:
					book.is_issued=False
					print("book returned")
					return
			else:
				print("book not found")
				
