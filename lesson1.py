# Simple Flight Booking System 

flights = [
    {"id": 1, "origin": "Tehran", "destination": "Mashhad", "price": 1200000, "seats": 5},
    {"id": 2, "origin": "Tehran", "destination": "Shiraz", "price": 1500000, "seats": 3},
    {"id": 3, "origin": "Isfahan", "destination": "Tehran", "price": 900000, "seats": 8},
]

bookings = []


def show_flights():
    print("\n--- Flight List ---")
    for flight in flights:
        print(f"Flight {flight['id']}: {flight['origin']} -> {flight['destination']} "
              f"| Price: {flight['price']} Toman | Seats available: {flight['seats']}")


def find_flight_by_id(flight_id):
    for flight in flights:
        if flight["id"] == flight_id:
            return flight
    return None


def book_flight():
    show_flights()
    flight_id = int(input("\nEnter the flight number you want to book: "))
    flight = find_flight_by_id(flight_id)

    if flight is None:
        print("No such flight exists!")
        return

    if flight["seats"] <= 0:
        print("Sorry, no seats available!")
        return

    passenger_name = input("Enter your name: ")

    flight["seats"] -= 1
    bookings.append({"passenger": passenger_name, "flight": flight})

    print(f"\nBooking successful! {passenger_name}, your ticket for the flight "
          f"from {flight['origin']} to {flight['destination']} has been booked.")


def view_bookings():
    if not bookings:
        print("\nNo bookings yet.")
        return

    print("\n--- Booking List ---")
    for i, booking in enumerate(bookings):
        flight = booking["flight"]
        print(f"{i + 1}. {booking['passenger']} - Flight {flight['origin']} to {flight['destination']}")


def cancel_booking():
    view_bookings()
    if not bookings:
        return

    index = int(input("\nEnter the booking number you want to cancel: "))

    if index < 1 or index > len(bookings):
        print("No such booking exists!")
        return

    booking = bookings.pop(index - 1)
    booking["flight"]["seats"] += 1

    print(f"\nBooking for {booking['passenger']} has been cancelled successfully.")


def main():
    while True:
        print("\n===== Flight Booking System =====")
        print("1. View flights")
        print("2. Book a flight")
        print("3. View bookings")
        print("4. Cancel a booking")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_flights()
        elif choice == "2":
            book_flight()
        elif choice == "3":
            view_bookings()
        elif choice == "4":
            cancel_booking()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()