-- CREATE  s trigger that resets the attribute "valid_email" only when the email has been changed
-- and the new email is valid.

DELIMITER //
CREATE TRIGGER valid_email_trigger
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        IF NEW.email IS NOT NULL THEN
            IF NEW.email REGEXP '^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$' THEN
                SET NEW.valid_email = 1;
            ELSE
                SET NEW.valid_email = 0;
            END IF;
        ELSE
            SET NEW.valid_email = 0;
        END IF;
    END IF;
END //
