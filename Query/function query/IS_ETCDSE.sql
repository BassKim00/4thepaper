DELIMITER $$

CREATE FUNCTION IS_ETCDSE(input text) RETURNS int
    DETERMINISTIC
BEGIN
    IF (input LIKE "%2%" OR
		input LIKE "%3%" OR
        input LIKE "%8%" OR
        input LIKE "%9%") THEN
        RETURN 1;
    ELSE
        RETURN 0;
	END IF;
END