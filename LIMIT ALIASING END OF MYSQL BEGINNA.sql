#LIMIT AND ALIASING
#WE WANT HOW MAY ROWS

SELECT *
FROM employee_demographics
LIMIT 3
;

# NOW WE WANT TO COMBINE LIKE TO GET THREE OLDEST PERSON
SELECT *
FROM employee_demographics
ORDER BY AGE desc
LIMIT 3
;

#SELEXTIN 
SELECT *
FROM employee_demographics
ORDER BY AGE desc
LIMIT 1,2
;


# ALIASING
SELECT gender, AVG(age) as AVG_AGE
FROM employee_demographics
GROUP BY gender
HAVING AVG(AGE)> 40
;



