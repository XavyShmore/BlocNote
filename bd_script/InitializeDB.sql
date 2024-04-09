CREATE TABLE users (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    email varchar(320) UNIQUE,
    passwordHash varchar(64),
    bio varchar(1000),
    name varchar(64)
);

CREATE TABLE notebooks (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    title varchar(100),
    creation DATETIME DEFAULT NOW(),
    owner_id INTEGER,
    FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE notes (
    id integer AUTO_INCREMENT PRIMARY KEY,
    title varchar(100)
);

CREATE TABLE versions (
    note_id integer not null,
    FOREIGN KEY (note_id) REFERENCES notes(id)  ON DELETE CASCADE,
    editor_id integer,
    FOREIGN KEY (editor_id) REFERENCES users(id) ON DELETE SET NULL,
    content MEDIUMTEXT,
    creation datetime DEFAULT NOW()
);

CREATE INDEX versions_index ON versions (note_id, creation, editor_id);

CREATE TABLE user_has_access (
    user_id integer not null,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    note_id integer NOT NULL,
    FOREIGN KEY (note_id) REFERENCES notes(id) ON DELETE CASCADE,
    UNIQUE (note_id, user_id)
);

CREATE TABLE notebook_contains(
    note_id integer NOT NULL,
    FOREIGN KEY (note_id) REFERENCES notes(id) ON DELETE CASCADE,
    notebook_id integer NOT NULL,
    FOREIGN KEY (notebook_id) REFERENCES notebooks(id) ON DELETE CASCADE,
    UNIQUE (note_id, notebook_id)
);