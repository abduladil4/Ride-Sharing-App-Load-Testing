from locust import HttpUser, task, between
import random

class RideUser(HttpUser):

    wait_time = between(1, 3)  # simulate real user think-time

    @task(3)
    def search_ride(self):
        pickup_locations = ["Hyderabad", "Gachibowli", "Madhapur", "Ameerpet", "KPHB"]
        drop_locations = ["Secunderabad", "Hi-Tech City", "LB Nagar", "Begumpet", "Kondapur"]

        pickup = random.choice(pickup_locations)
        drop = random.choice(drop_locations)

        self.client.get(
            "/search_ride",
            params={"pickup": pickup, "drop": drop},
            name="Search Ride"
        )

    @task(2)
    def book_ride(self):
        pickup = random.choice(["Hyderabad", "Madhapur"])
        drop = random.choice(["KPHB", "Gachibowli"])

        self.client.post(
            "/book_ride",
            json={"pickup": pickup, "drop": drop},
            name="Book Ride"
        )

    @task(1)
    def complete_ride(self):
        ride_id = random.randint(1_
