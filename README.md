### A sample flight searching app using Amadeus API sdk + Flask, Htnl

This is a simple app that shows how to use the [Amadeus Python SDK](https://github.com/amadeus4dev/amadeus-python) with a Flask web interface.  
It allows users to search for flight offers by entering origin, destination, date, passenger count, currency, and whether to filter for direct flights only.


---

#### Setup

1. Activate your virtual enviroment:
```bash
source venv/bin/activate        # Linux / Mac
venv\Scripts\activate           # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a .env file in the project root and add your Amadeus credentials:
```bash
AMADEUS_CLIENT_ID=your_client_id
AMADEUS_CLIENT_SECRET=your_client_secret
```

---

```bash
URL: Run and go to http://127.0.0.1:5000/
```







