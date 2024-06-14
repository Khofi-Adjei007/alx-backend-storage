-- This script creates a trigger to reset valid_email only when the email has been changed.

DELIMITER //

CREATE TRIGGER update_valid_email_trigger
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END//

DELIMITER ;
