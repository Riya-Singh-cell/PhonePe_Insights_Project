CREATE TABLE aggregated_insurance (
    id SERIAL PRIMARY KEY,
    year INT,
    quarter INT,
    from_timestamp BIGINT,
    to_timestamp BIGINT,
    name VARCHAR(50),
    type VARCHAR(20),
    count INT,
    amount FLOAT
);
