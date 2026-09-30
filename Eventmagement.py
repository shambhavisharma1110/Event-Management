def create_event():
    name = input("Enter event name: ")
    date = input("Enter event date: ")
    print("Event created successfully!")
    print("Event:", name)
    print("Date:", date)
def view_events():
    print("\n--- EVENTS ---")
    print("1. College Fest - 10 October")
    print("2. Sports Day - 15 October")
    print("3. Cultural Night - 20 October")
def register():
    name = input("Enter participant name: ")
    event = input("Enter event name: ")
    print(name, "registered for", event)
def view_participants():
    print("\n--- PARTICIPANTS ---")
    print("1. Rahul - College Fest")
    print("2. Priya - Sports Day")
def update_event():
    event = input("Enter event name: ")
    new_date = input("Enter new date: ")
    print(event, "date updated to", new_date)
def cancel_event():
    event = input("Enter event name to cancel: ")
    print(event, "has been cancelled.")
def exit_program():
    print("Thank you for using Event Management System!")
while True:
    print("\n===== EVENT MANAGEMENT =====")
    print("1. Create Event")
    print("2. View Events")
    print("3. Register Participant")
    print("4. View Participants")
    print("5. Update Event")
    print("6. Cancel Event")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_event()
    elif choice == "2":
        view_events()
    elif choice == "3":
        register()
    elif choice == "4":
        view_participants()
    elif choice == "5":
        update_event()
    elif choice == "6":
        cancel_event()
    elif choice == "7":
        exit_program()
        break
    else:
        print("Invalid choice!")