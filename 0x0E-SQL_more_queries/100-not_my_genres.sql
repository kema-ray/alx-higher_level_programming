-- Lists all the genres of the database
-- Records are sorted by ascennding genre name

SELECT DISTINCT `name`
  FROM `tv_genres` AS i
       INNER JOIN `tv_show_genres` AS s
       ON i.`id` = s.`genre_id`

       INNER JOIN `tv_shows` AS t
       ON s.`show_id` = t.`id`
       WHERE i.`name` NOT IN
             (SELECT `name`
                FROM `tv_genres` AS i
	             INNER JOIN `tv_show_genres` AS s
		     ON i.`id` = s.`genre_id`

		     INNER JOIN `tv_shows` AS t
		     ON s.`show_id` = t.`id`
		     WHERE t.`title` = "Dexter")
 ORDER BY i.`name`;
