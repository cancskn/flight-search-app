
from flask import Flask, render_template, request
from amadeus import Client,ResponseError
from dotenv import load_dotenv
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

load_dotenv()
app = Flask(__name__)
amadeus = Client()

def parse_date_input(depart_value, depart_unit, depart_date):
    # If input was a certain date
    if depart_date:
        return depart_date.strip()
    # If number 
    if depart_value:
        value = int(depart_value)
        if depart_unit == "days":
            return (datetime.today() + timedelta(days=value)).strftime("%Y-%m-%d")
        elif depart_unit == "months":
            return (datetime.today() + relativedelta(months=value)).strftime("%Y-%m-%d")
    # No date
    return None


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    origin = request.form["origin"].upper()
    destination = request.form["destination"].upper()

    depart_value = request.form.get("depart_value")
    depart_unit = request.form.get("depart_unit")
    depart_date_text = request.form.get("depart_date")

    depart_date = parse_date_input(depart_value, depart_unit, depart_date_text)

    adults = int(request.form["adults"])
    direct = request.form["direct"].upper()
    currency = request.form["currency"].upper()

    flights = []
    try:
        print("PARAMS:", origin, destination, depart_date, adults, currency)

        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=depart_date,
            adults=adults,
            currencyCode=currency,
            max=10
        )
        data = response.data

        # Direct flights filter
        if direct == "YES":
            flights = [f for f in data if len(f["itineraries"][0]["segments"]) == 1]
        else:
            flights = data

    except ResponseError as e:
        flights = []
        print("Error:", e.response.status_code, e.response.body)
    
    return render_template("index.html", flights=flights)

if __name__ == "__main__":
    app.run(debug=True)