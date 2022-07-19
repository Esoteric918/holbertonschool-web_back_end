-- Create a stored procedure AddBonus that adds a new correction for a student
-- The procedure should take the following parameters:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
-- project_name, a new or already exists projects - if no projects.name found in the table, you should create it
-- score, the score value for the correction

DELIMITER //
CREATE
    PROCEDURE AddBonus (
        IN user_id INT,
        IN project_name VARCHAR(255),
        IN score FLOAT
    )
BEGIN
    INSERT INTO projects (name)
    SELECT project_name from DUAL
    WHERE NOT EXISTS (SELECT * FROM projects WHERE name = project_name);

    SELECT id INTO @pro_id FROM projects WHERE name = project_name;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, @pro_id, score);
END;
//
