def add(a,b):
    return a+b
print(add(10,20))



def add(age,name):
    return age,name 
print(add("mani",21))

def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")

greet("Bob")            
greet("Bob", "Good morning")


def table(num, upto=10):
    print(f"Table of {num}:")
    for i in range(1, upto + 1):
        print(f"{num} x {i} = {num * i}")

table(5)     
table(5, 15)  


def student_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")
student_info(age=20, city="Delhi", name="Alice")


def info(name, age=18, city='Unknown'):
    print(f"Name: {name}, Age: {age}, City: {city}")
info("John")                         
info("John", 25)                     
info("John", city="Mumbai")          
info("John", 30, "New York") 


def book_ticket(name, train='Express', seat='Sleeper', fare=500):
    print(f"Ticket: {name} | Train: {train} | Seat: {seat} | Fare: {fare}")

book_ticket("Rahul")                                      
book_ticket("Rahul", "Rajdhani")                          
book_ticket(name="Rahul", train="Shatabdi", fare=1200)  



def bill(item, qty=1, price=100, discount=0):
    total = (qty * price) - discount
    print(f"Item: {item} | Total: {total}")

bill("Book")                               
bill("Pen", 5)                             
bill("Laptop", price=50000, discount=2000) 


def area(length, width=10, unit='sq.m'):
    result = length * width
    print(f"Area: {result} {unit}")

area(5)              
area(5, 20)           
area(5, 20, 'sq.ft')  



def flight_booking(name, source, destination, airline='IndiGo', seat='Economy'):
    print(f"Pass: {name} | Route: {source}->{destination} | Airline: {airline} | Seat: {seat}")
flight_booking("Amit", "Mumbai", "Goa")
flight_booking("Amit", "Mumbai", "Goa", airline="Air India", seat="Business")
flight_booking("Amit", "Delhi", "Dubai", seat="First Class")

