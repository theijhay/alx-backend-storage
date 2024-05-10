-- Computes and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
    DECLARE total_weighted_score_for_user INT DEFAULT 0;
    DECLARE user_id_var INT DEFAULT 0;

    SELECT SUM(corrections.score * projects.weight)
        INTO total_weighted_score_for_user
        FROM corrections
            INNER JOIN projects
                ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

    SELECT SUM(projects.weight)
        INTO user_id_var
        FROM corrections
            INNER JOIN projects
                ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

    IF user_id_var = 0 THEN
        UPDATE users
            SET users.average_score = 0
            WHERE users.id = user_id;
    ELSE
        UPDATE users
            SET users.average_score = total_weighted_score_for_user / user_id_var
            WHERE users.id = user_id;
    END IF;
END $$
DELIMITER ;

