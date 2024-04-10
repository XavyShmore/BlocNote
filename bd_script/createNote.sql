CREATE PROCEDURE create_note (
    IN title VARCHAR(255),
    IN user_id INT
)
BEGIN
    DECLARE note_id INT;

    INSERT INTO notes (title) VALUE (title);
    SET note_id = LAST_INSERT_ID();
    INSERT INTO user_has_access (user_id, note_id) VALUE (user_id, note_id);
    INSERT INTO versions (note_id, editor_id, content) VALUE (note_id, user_id, '');
end;
