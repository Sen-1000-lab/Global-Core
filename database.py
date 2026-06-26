CREATE TABLE IF NOT EXISTS notifications (

    id SERIAL PRIMARY KEY,

    user_id BIGINT,

    title TEXT,

    content TEXT,

    read BOOLEAN DEFAULT FALSE,

    created_at TIMESTAMP DEFAULT NOW()

)
