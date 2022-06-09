from library_management_system import *
from faker import Faker
from faker.providers import DynamicProvider
import logging

subject_provider = DynamicProvider(
     provider_name="subjects",
     elements=["development", "programming", "networking", "operating system"])

language_provider = DynamicProvider(
     provider_name="languages",
     elements=["Java", "python", "nodejs", "golang"])

title_provider = DynamicProvider(
     provider_name="titles",
     elements=["Learn", "mastering", "hands on ", "beginner"])  

publisher_provider = DynamicProvider(
     provider_name="publishers",
     elements=["o`really", "packtPub", "Leanpub"]) 

authors_provider = DynamicProvider(
     provider_name="authors",
     elements=["Robert C", "Steve McConnell", "Frederick Brooks", "Jon Stokes"]) 

fake = Faker()
# then add new providers to faker instance
fake.add_provider(subject_provider)
fake.add_provider(language_provider)
fake.add_provider(title_provider)
fake.add_provider(publisher_provider)
fake.add_provider(authors_provider)

def generateBooks(number):
    books=[]
    for i in range(number):
        book = Book(fake.isbn10(),fake.titles()+ " " +fake.languages(),fake.subjects(),fake.publishers(), 
                "english",fake.random_number(digits=3,fix_len=True),fake.authors())
        books.append(book)              
    return books

def generateBookItems(number, books, racks):
    book_items= []
    for i in range(number):
        random_book = fake.random_element(books)
        random_rack = fake.random_element(racks)
        random_bool = fake.random_element([True,False])
        book_item = BookItem(*vars(random_book).values(),fake.ean(length=13), False, random_bool,
          None,fake.random_number(digits=4,fix_len=True),BookStatus.AVAILABLE, None, None,random_rack)
        book_items.append(book_item)              
    return book_items

def generateMembers(number):
    members = []
    for i in range(number):
        first_name = fake.first_name_male()
        last_name = fake.last_name()
        email = f"{first_name}.{last_name}@{fake.domain_name()}"
        person = Person ( first_name+ " "+last_name, fake.address(),email, fake.phone_number())
        account = Account(100+i,fake.password(),person )
        member = Member(*vars(account).values())
        members.append(member)
    return members

def runSimulator(n, members, book_items):
    all_loaned_book_items = []
    total_loaned = 0
    total_retruned = 0
    for i in range(n):
        random_operation = fake.random_element(['checkout', 'return'])
        if random_operation == "checkout":
            random_member= fake.random_element(members)
            random_book_item= fake.random_element(book_items)
            result = random_member.checkout_book_item(random_book_item , fake.date_this_year(False,True))
            if result :
                all_loaned_book_items.append(result)
                total_loaned = total_loaned +1
        
        if random_operation == "return":
            if all_loaned_book_items :
               random_loaned = fake.random_element(all_loaned_book_items)
               loaned_member_id = random_loaned.member_id
               book_item_barcode = random_loaned.book_item_barcode
               member = next(filter(lambda member: member.id == loaned_member_id, members))
               book_item = next(filter(lambda book: book.barcode == book_item_barcode, book_items))
               member.return_book_item(book_item)
               all_loaned_book_items.remove(random_loaned)
               total_retruned= total_retruned +1
            else:
                print ("No book is currently Loaned")
    print (total_loaned, total_retruned, len(all_loaned_book_items))            
                   


def main():
    number_of_books, number_of_book_items, number_of_member = 10,50,5
    racks = [Rack(1, "row 1 left rack"), Rack(2, "row 1 right rack")]
    books = generateBooks(number_of_books)
    bookitems= generateBookItems(number_of_book_items,books, racks)
    members = generateMembers(number_of_member)
    runSimulator(100, members, bookitems)
    

if __name__ == "__main__":
    main()

    