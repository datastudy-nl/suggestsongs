CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(255) PRIMARY KEY,
    display_name VARCHAR(1000),
    email VARCHAR(1000),
    product VARCHAR(1000),
    country VARCHAR(1000),
    image VARCHAR(1000)
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
    image VARCHAR(1000),
    preview_url VARCHAR(1000),
    uri VARCHAR(1000),
    FOREIGN KEY (id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS track_rating (
    track_id VARCHAR(255),
    user_id VARCHAR(255),
    rating INT,
    PRIMARY KEY (track_id, user_id),
    FOREIGN KEY (track_id) REFERENCES tracks(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);