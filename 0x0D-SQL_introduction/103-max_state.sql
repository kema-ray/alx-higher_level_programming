-- script that displays the max temperature of each state
-- Query to display the max temperature of each state

SELECT state, MAX(value) as max_temp FROM temperatures
GROUP BY state
ORDER BY state
limit 3;
