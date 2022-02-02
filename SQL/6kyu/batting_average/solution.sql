SELECT player_name, games, CAST(ROUND((hits+0.0)/at_bats, 3) AS TEXT) AS batting_average
FROM yankees
WHERE at_bats >= 100
ORDER BY 3 DESC;
