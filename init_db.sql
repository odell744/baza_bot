-- BOT INIT SCRIPT FOR BAZA BOT
-- INFORMATION ABOUT VERSION OF SCRIPT AND ETC AT BOTTOM


CREATE TABLE IF NOT EXISTS roles
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    desc TEXT NOT NULL
);
-- default bot roles
INSERT OR REPLACE INTO roles VALUES (0, "user", "user_desc"),
                                    (1, "moder", "moder_desc"),
                                    (2, "admin", "admin_desc"),
                                    (3, "owner", "owner_desc");
-- maybe need some restruct in future, but now seems pretty ok
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    role INTEGER,
    FOREIGN KEY (role)  REFERENCES roles (id)
);
-- ====================================== --
--               GOODS INFO               --
-- ====================================== --
CREATE TABLE IF NOT EXISTS goods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT
);
-- attributes for goods
-- such as size, weight etc
CREATE TABLE IF NOT EXISTS goods_attributes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,          -- attribute name
    description TEXT    -- attribute description
);



INSERT OR REPLACE INTO goods_attributes VALUES  (0, "size", "size_desc"),
                                                (1, "weight", "weight_desc"),
                                                (2, "color", "color_desc"),
                                                (3, "fabricue_country", "fabricue_country_desc");



CREATE TABLE IF NOT EXISTS bot_info
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    desc TEXT NOT NULL,
    version TEXT NOT NULL
);
INSERT OR REPLACE INTO bot_info VALUES
(0, "first version", "common starting point for bot", "1.0.0");