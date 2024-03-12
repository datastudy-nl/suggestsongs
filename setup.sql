CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(255) PRIMARY KEY,
    display_name VARCHAR(1000),
    email VARCHAR(1000),
    product VARCHAR(1000),
    country VARCHAR(1000),
    image VARCHAR(1000)
);

CREATE TABLE IF NOT EXISTS logins (
    user_id VARCHAR(255),
    date TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS authentication (
    id VARCHAR(255) PRIMARY KEY,
    access_token VARCHAR(1000),
    refresh_token VARCHAR(1000),
    FOREIGN KEY (id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS tracks (
    id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(1000),
    artist VARCHAR(1000),
    album VARCHAR(1000),
    duration_ms VARCHAR(1000),
    popularity VARCHAR(1000),
    explicit VARCHAR(1000),
    url VARCHAR(1000)
);


CREATE TABLE IF NOT EXISTS track_rating (
    track_id VARCHAR(255),
    user_id VARCHAR(255),
    rating INT,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (track_id, user_id),
    FOREIGN KEY (track_id) REFERENCES tracks(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS audio_features (
    track_id VARCHAR(255) PRIMARY KEY,
    danceability FLOAT,
    energy FLOAT,
    key_ INT,
    loudness FLOAT,
    mode INT,
    speechiness FLOAT,
    acousticness FLOAT,
    instrumentalness FLOAT,
    liveness FLOAT,
    valence FLOAT,
    tempo FLOAT,
    duration_ms INT,
    time_signature INT,
    FOREIGN KEY (track_id) REFERENCES tracks(id)
);

CREATE TABLE IF NOT EXISTS feedback (
    user_id VARCHAR(255),
    feedback VARCHAR(1000),
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);