DROP TRIGGER IF EXISTS delete_orphan_notes_when_access_deleted;
DROP TRIGGER IF EXISTS delete_orphan_notes_when_parent_deleted;

DROP PROCEDURE IF EXISTS create_note;

DROP TABLE IF EXISTS user_as_access;
DROP TABLE IF EXISTS user_has_access;

DROP TABLE IF EXISTS notebook_contains;

DROP TABLE IF EXISTS versions;

DROP TABLE IF EXISTS notes;

DROP TABLE IF EXISTS notebooks;

DROP TABLE IF EXISTS users;