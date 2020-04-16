CREATE TABLE flights(
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duaration INTEGER NOT NULL,
    duration INTEGER NOT NULL
);