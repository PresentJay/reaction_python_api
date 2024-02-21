-- users 테이블 생성
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    flavor_genre_first VARCHAR(255),
    flavor_genre_second VARCHAR(255),
    flavor_genre_third VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- game_music 테이블 생성
CREATE TABLE IF NOT EXISTS game_music (
    id SERIAL PRIMARY KEY,
    link_fragment VARCHAR(255) UNIQUE,
    genre_name VARCHAR(255),
    creator_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- game_result 테이블 생성
CREATE TABLE IF NOT EXISTS game_result (
    player_id INTEGER,
    music_id INTEGER,
    score INTEGER,
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
