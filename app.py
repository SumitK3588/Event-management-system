from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock Database (In production, use SQLite or PostgreSQL)
events = [
    {
        "id": 1,
        "name": "Tech Conference 2026",
        "date": "2026-06-15",
        "tickets_sold": 120,
    },
    {"id": 2, "name": "AI Workshop", "date": "2026-07-20", "tickets_sold": 45},
]


@app.route("/")
def dashboard():
    # Analytics & Reporting: Calculate total metrics for the UI
    total_events = len(events)
    total_tickets = sum(e["tickets_sold"] for e in events)
    return render_template(
        "/Users/sumitmanandhar/Desktop/SS-ASSIGNMENT/index.html",
        events=events,
        total_events=total_events,
        total_tickets=total_tickets,
    )


@app.route("/create", methods=["GET", "POST"])
def create_event():
    if request.method == "POST":
        # Event Creation Logic
        new_event = {
            "id": len(events) + 1,
            "name": request.form.get("name"),
            "date": request.form.get("date"),
            "tickets_sold": 0,
        }
        events.append(new_event)
        return redirect(url_for("dashboard"))
    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)
