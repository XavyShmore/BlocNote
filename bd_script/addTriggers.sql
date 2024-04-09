CREATE TRIGGER delete_orphan_notes_when_access_deleted
    AFTER DELETE ON user_as_access
    FOR EACH ROW
        BEGIN
            DECLARE has_remaining_access INT DEFAULT 0;

            SELECT COUNT(*) INTO has_remaining_access
            FROM user_as_access
            WHERE note_id = OLD.note_id;

            IF has_remaining_access = 0 THEN
                DELETE FROM notes WHERE id = OLD.note_id;
            end if;
        end;

CREATE TRIGGER delete_orphan_notes_when_parent_deleted
    BEFORE DELETE ON users
    FOR EACH ROW
        BEGIN
            DELETE FROM notes
            WHERE notes.id
            IN (SELECT has_access_notes.note_id
                FROM (SELECT note_id, COUNT(*) as count
                      FROM user_as_access
                      WHERE note_id IN
                            (SELECT u.note_id
                             FROM user_as_access u
                             WHERE ID = user_id)
                      GROUP BY note_id) as has_access_notes
                WHERE has_access_notes.count = 1);
        end;