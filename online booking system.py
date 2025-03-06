from random import *

def main():
    print("<---------WELCOME TO TICKET BOOKING--------------->")
    menu()

tickets = []

def book():
    ch = int(input("How many tickets do you want to book?: "))
    date = input("Enter Departure Date (YYYY-MM-DD): ")
    start = input("Enter Starting Station: ")
    end = input("Enter Ending Station: ")
    
    for i in range(ch):
        name = input("Traveller name: ")
        age = input("Enter traveller age: ")
        temp = [name, age, date, start, end]
        tickets.append(temp)
        print(f"Ticket {i+1} Booked: {temp}")
    
    print("All tickets booked. Now go to the generate section and get your ticket.")
    print("=======================")
    menu()

def cancel():
    if not tickets:
        print("No tickets to cancel.")
        menu()
        return
    
    print("Your Tickets:")
    for i, ticket in enumerate(tickets, start=1):
        print(f"{i}. {ticket}")
    
    ch = int(input("Enter ticket number to cancel: "))
    if 1 <= ch <= len(tickets):
        tickets.pop(ch - 1)
        print("1 ticket cancelled")
    else:
        print("Invalid selection. Please try again.")
    
    print("==================")
    menu()

def menu():
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        book()
    elif choice == '2':
        cancel()
    elif choice == '3':
        print("Thank you for using the ticket booking system!")
        exit()
    else:
        print("Invalid choice, try again.")
        menu()

if __name__ == "__main__":
    main()
