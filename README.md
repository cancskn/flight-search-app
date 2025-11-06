### Flight Search App using Amadeus API + Flask

A simple Flask web application that lets users search flight offers by origin, destination, date, passenger count, currency, and direct-flight preference. Results appear below the form on the same page.

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
URL: http://127.0.0.1:5000/
```







