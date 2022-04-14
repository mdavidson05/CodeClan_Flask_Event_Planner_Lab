from flask import render_template, request # ADDED
from app import app
from models.event_class import Event
from models.events import *


@app.route('/')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/add_event', methods=['POST'])
def add_event():
    # print(request.form) #prints to terminal, use for debugging
    event_date = request.form["date"]
    event_name = request.form["name"]
    event_guest_number = request.form["Number of Guests"]
    event_room_location = request.form["Room location"]
    event_description = request.form["description"]
    for event in request.form:
        # print(event)
        if "recurring" in request.form:
            event_recurring = True
        else:
            event_recurring = False
    # print(event_name)
    # print(event_description)
    # print(event_recurring)
    new_event = Event(event_date,event_name, event_guest_number, event_room_location, event_description,event_recurring)
    add_new_event(new_event)
    # print(new_event)
    return render_template('index.html', title = "Home", events = events)

@app.route('/delete/<index>', methods = ['POST'])
def delete_event(index):
    print(events)
    chosen_event = events[int(index)]
    remove_event(chosen_event)
    print(events)
    return render_template('index.html')