CREATE TABLE drivers (
    driver_id INT PRIMARY KEY,
    name VARCHAR(50),
    rating FLOAT
);

CREATE TABLE rides (
    ride_id INT PRIMARY KEY,
    user_id INT,
    driver_id INT,
    pickup VARCHAR(100),
    drop_location VARCHAR(100),
    fare INT,
    status VARCHAR(20)
);
