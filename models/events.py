from models.event_class import *

event1 = Event("12/05/2022","Hackathon", 200, "London", "Coding Challenge", True)

event2 = Event("14/06/2022","CodeClan Alumni", 50, "Edinburgh", "Drinks and talks", False)

events = [event1,event2]

def add_new_event(event):
    events.append(event)

def remove_event(event):
    events.remove(event)