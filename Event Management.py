class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def add_participant(self,date, name):
        self.participants.append(date, name)

    def get_count(self):
        print(self.participants.len())

participants = {}

def add(date, name):
    participants[date] = Event(date, name)

def count():
    print(len(participants))

while True:
    choice = input("Do you want to 'add' or 'count'? ")
    if choice == "add":
        date = input("Date: ")
        name = input("Name: ")
        add(date, name)
    elif choice == "count":
        count()
