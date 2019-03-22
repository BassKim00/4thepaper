DELIMITER $$

CREATE FUNCTION CONV_SMK(input1 text,input2 text) RETURNS int
    DETERMINISTIC
BEGIN
	IF input1+input2=0 THEN
		RETURN 0;
	ELSEIF input1+input2 <5 THEN
		RETURN 1;
	ELSEIF input1+input2 <10 THEN
		RETURN 2;
	ELSEIF input1+input2 <20 THEN
		RETURN 3;
	ELSEIF input1+input2 <30 THEN
		RETURN 4;
	ELSE
		RETURN 5;
	END IF;
END