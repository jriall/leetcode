-- Grand Slam Titles

-- SQL Schema
-- Table: Players

-- +----------------+---------+
-- | Column Name    | Type    |
-- +----------------+---------+
-- | player_id      | int     |
-- | player_name    | varchar |
-- +----------------+---------+
-- player_id is the primary key for this table.
-- Each row in this table contains the name and the ID of a tennis player.
 

-- Table: Championships

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | year          | int     |
-- | Wimbledon     | int     |
-- | Fr_open       | int     |
-- | US_open       | int     |
-- | Au_open       | int     |
-- +---------------+---------+
-- year is the primary key for this table.
-- Each row of this table containts the IDs of the players who won one each
-- tennis tournament of the grand slam.
 

-- Write an SQL query to report the number of grand slam tournaments won by each
-- player. Do not include the players who did not win any tournament.

-- Return the result table in any order.

SELECT
    p.player_id, 
    p.player_name, 
    SUM(IF(c.Wimbledon = p.player_id, 1, 0) + 
        IF(c.Fr_open = p.player_id, 1, 0) + 
        IF(c.US_open = p.player_id, 1, 0) + 
        IF(c.Au_open = p.player_id, 1, 0)) AS grand_slams_count
FROM
    Players AS p,
    Championships AS c
GROUP BY
    p.player_id
HAVING
    grand_slams_count > 0
