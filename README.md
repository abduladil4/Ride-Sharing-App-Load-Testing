# Ride-Sharing-App-Load-Testing
Ride-Sharing Load Testing Framework using Locust, JMeter, Python &amp; Flask API. Simulates riders, drivers &amp; real-time trip events under heavy load.
 Ride-Sharing App Load Testing
Locust + JMeter + Python + Flask API

A fully simulated ride-sharing application (similar to Uber/Ola) designed for performance testing using Locust, JMeter, and a Python Flask API.
This project tests the system with riders, drivers, trip creation, location updates, and fare calculations under heavy load.

🧱 Features

Rider + Driver simulation

Trip workflow (request → accept → complete)

Real-time driver location updates

Load testing with:

✔ Locust

✔ JMeter

Sample dataset

SQL schema

Flask backend

Perfect for interviews + GitHub portfolio

📁 Project Structure
ride-sharing-load-test/
│
├── README.md
├── requirements.txt
│
├── api/
│   ├── app.py
│   ├── database.sql
│   └── sample_rides.csv
│
├── locust/
│   └── ride_test.py
│
└── jmeter/
    └── ride_test.jmx

🚀 How to Run the Project
1️⃣ Install Requirements
pip install -r requirements.txt

2️⃣ Start the Flask API
cd api
python app.py


Backend runs at:

http://127.0.0.1:5000

3️⃣ Run Locust Load Test
cd locust
locust -f ride_test.py


Open UI:

http://localhost:8089


Enter:

Number of users

Spawn rate

Host → http://127.0.0.1:5000

4️⃣ Run JMeter Test

Open Apache JMeter

File → Open → choose:

jmeter/ride_test.jmx


Set server URL:

http://127.0.0.1:5000


Run test (Ctrl + R)

🌐 API Endpoints
Method	Endpoint	Description
POST	/rider/request_trip	Rider requests a ride
POST	/driver/update_loc	Driver location update
POST	/trip/accept	Accept ride request
POST	/trip/complete	End ride + calculate fare
GET	/health	Health check
📊 What You Can Measure

RPS (Requests per second)

Response latency

Failure rate

API bottlenecks

Database stress

Concurrency effects

Rider vs driver load patterns

🛠 Tech Stack

Python

Flask

Locust

JMeter

Pandas

SQLite/MySQL (optional)

💡 Why This Project Is Useful

Real-world performance testing example

Unique GitHub portfolio project

Helps with QA/Performance Testing roles

Great for interview discussions

Shows Locust + JMeter + Python skills

Future Enhancements

Add Redis caching

Add JWT authentication

Add driver auto-match AI

Add Grafana dashboard for metrics

Add containerization (Dockerfile + Compose)

Author
Created by: <Md Abdul Adil>
Email: <mdabduladil4@gmail>
GitHub: <https://github.com/abduladil4>
