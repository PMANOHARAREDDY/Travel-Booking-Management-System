from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

buses = [
    {"id": 1, "name": "Belagavi-Davanagere", "available_seats": 50},
    {"id": 2, "name": "Hubballi-Davanagere", "available_seats": 40},
    {"id": 3, "name": "Echalakarnaji-Davanagere", "available_seats": 30},
    {"id": 4, "name": "Ballari-Talur", "available_seats": 48},
    {"id": 5, "name": "Ballari-Holagunda", "available_seats": 43},
    {"id": 6, "name": "Ballari-Siruguppa", "available_seats": 50},
    {"id": 7, "name": "Ballari-Bangalore", "available_seats": 47},
    {"id": 8, "name": "Talur-Bangalore", "available_seats": 36},
    {"id": 9, "name": "Talur-Hyderabad", "available_seats": 50},
    {"id": 10, "name": "Talur-New Delhi", "available_seats": 50},
    {"id": 11, "name": "Talur-Guwahatti", "available_seats": 50},
    {"id": 12, "name": "Talur-Bombay", "available_seats": 39},
    {"id": 13, "name": "Talur-Chennai", "available_seats": 48},
    {"id": 14, "name": "Talur-Kanyakumari", "available_seats": 50},
    {"id": 15, "name": "Talur-Madhalaghatty", "available_seats": 39},
    {"id": 16, "name": "Madhalaghatty-Talur", "available_seats": 50},
    {"id": 17, "name": "Talur-Karachi", "available_seats": 47},
    {"id": 18, "name": "Talur-Las_Vegas", "available_seats": 58},
    {"id": 19, "name": "New_York-Talur", "available_seats": 50},
    {"id": 20, "name": "Moscow-Talur", "available_seats": 52},

]

bookings = []

@app.route("/")
def index():
    return render_template("index.html", buses=buses)

@app.route("/book/<int:bus_id>", methods=["GET", "POST"])
def book(bus_id):
    if request.method == "POST":
        name = request.form["name"]
        seats = int(request.form["seats"])
        bus = next((bus for bus in buses if bus["id"] == bus_id), None)
        if bus and seats <= bus["available_seats"]:
            booking = {"name": name, "seats": seats, "bus_id": bus_id}
            bookings.append(booking)
            bus["available_seats"] -= seats
            return redirect(url_for("index"))
    return render_template("book.html", bus=next((bus for bus in buses if bus["id"] == bus_id), None))

@app.route('/view_bookings')
def view_bookings():
    # Logic to retrieve bookings (e.g., from a database)
    bookings = get_bookings()  # Replace with your actual data retrieval logic
    return render_template("bookings.html", bookings=bookings, get_bus_name=get_bus_name)


@app.template_filter('get_bus_name')
def get_bus_name(bus_id):
    bus = next((bus for bus in buses if bus["id"] == bus_id), None)
    return bus["name"] if bus else "Unknown Bus"

if __name__ == "__main__":
    app.run(debug=True)
