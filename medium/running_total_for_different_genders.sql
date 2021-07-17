SELECT
  gender,
  day,
  (
    SELECT
      SUM(score_points)
    FROM
      Scores t
    WHERE
      s.gender = t.gender
    AND
      s.day >= t.day
  ) AS total
FROM
  Scores s
ORDER BY
  gender,
  day
