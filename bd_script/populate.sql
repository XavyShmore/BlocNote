INSERT INTO users (email, passwordHash, name, bio)
VALUES
    ('xavier.hamel.5@ulaval.ca', 'aHgyayYBkjKJGUYBV', 'Xavier Hamel', 'Je suis un étudiant en génie logiciel qui adore les bases de données'),
    ('marie.tremblay.12@uqam.ca', 'kjahsdlkjashdlkjashdlkj', 'Marie Tremblay', 'Je suis une passionnée de cuisine et de voyages'),
    ('jean.dupont.34@hotmail.com', 'lkjhasdlkjashdlkjashdlkj', 'Jean Dupont', 'Je suis un entrepreneur dans le domaine des technologies'),
    ('sophie.martin.56@gmail.com', 'lkjhasdlkjashdlkjashdlkj', 'Sophie Martin', 'Je suis une artiste peintre et illustratrice'),
    ('alexandre.charest.78@yahoo.ca', 'lkjhasdlkjashdlkjashdlkj', 'Alexandre Charest', 'Je suis un musicien et compositeur'),
    ('isabelle.gagnon.90@outlook.com', 'lkjhasdlkjashdlkjashdlkj', 'Isabelle Gagnon', 'Je suis une professeure de yoga et de méditation'),
    ('samuel.levesque.102@icloud.com', 'lkjhasdlkjashdlkjashdlkj', 'Samuel Levesque', 'Je suis un ingénieur en mécanique'),
    ('camille.robert.114@bell.net', 'lkjhasdlkjashdlkjashdlkj', 'Camille Robert', 'Je suis une avocate spécialisée en droit familial'),
    ('olivier.richard.126@videotron.ca', 'lkjhasdlkjashdlkjashdlkj', 'Olivier Richard', 'Je suis un développeur web et mobile'),
    ('elodie.pilon.138@rogers.com', 'lkjhasdlkjashdlkjashdlkj', 'Élodie Pilon', 'Je suis une graphiste et webdesigner'),
    ('shrek.shrek@shrek.tv', 'lkjhasdlkjashdlkjashdlkj', 'Shrek', 'Je suis un ogre vert qui vit dans un marais');

INSERT INTO notes (title)
VALUE ('This will be a greate note');
CALL create_note('This will be a great note', 1);
CALL create_note('J\'aime ta grand mère !!!', 3);
CALL create_note('Pipi, caca, popo: la meilleure des chansons', 3);

INSERT INTO user_has_access (user_id, note_id)
VALUES (2,1),
       (3,1),
       (4,1),
       (5,2);