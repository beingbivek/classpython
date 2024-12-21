age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
show_type = input("Enter the show type (Matinee/Evening): ").capitalize()

if 0 < age < 12:
    if show_type == "Matinee":
        ticket_price = 500
    elif show_type == "Evening":
        ticket_price = 700
elif 12 <= age < 60:
    if gender == 'M':
        if show_type == "Matinee":
            ticket_price = 800
        elif show_type == "Evening":
            ticket_price = 1000
    elif gender == 'F':
        if show_type == "Matinee":
            ticket_price = 700
        elif show_type == "Evening":
            ticket_price = 900
elif age >= 60:
    ticket_price = 600
else:
    ticket_price = 1

if ticket_price == 1:
    print("Invalid Age!")
else:
    print("Ticket price: ", ticket_price)
