DELIMITER //

-- Create stored procedure ComputeAverageScoreForUser
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE total_count INT DEFAULT 0;
    DECLARE avg_score FLOAT DEFAULT 0;

    -- Calculate total score and count of corrections for the user
    SELECT SUM(score), COUNT(*) INTO total_score, total_count FROM corrections WHERE user_id = user_id;

    -- Calculate average score
    IF total_count > 0 THEN
        SET avg_score = total_score / total_count;
    END IF;

    -- Update the user's average_score in the users table
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END;

//
DELIMITER ;

