from flask import Blueprint, request, jsonify
# from .models.post import db, Event
# routes/event.py
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.post import db, Event ,Birthday

event_bp = Blueprint('events', __name__)

@event_bp.route('/create_event', methods=["GET"])
def create_event():
    bid = request.args.get("bid")
    bname = request.args.get("name")
    return render_template('create_event.html', bid=bid, name=bname)

# Create a new event associated with a birthday
@event_bp.route('/create_event_data', methods=["POST"])
def create_event_data():
    title = request.form['title']
    bid = request.form['bid']
    new_event = Event(title=title, birthday_id=bid)
    db.session.add(new_event)
    db.session.commit()
    return {'data':'event created successfully'}


# Delete past events associated with birthdays
@event_bp.route('/delete-past-events', methods=['GET'])
def delete_past_events():
    try:
        # Get the current date and time
        current_datetime = datetime.now()

        # Query and delete past events
        past_events = Event.query.filter(Event.date < current_datetime.date()).all()
        for event in past_events:
            db.session.delete(event)

        db.session.commit()

        return jsonify({"message": "Past events deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


