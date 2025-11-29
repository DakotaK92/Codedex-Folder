SELECT * FROM students;
SELECT * FROM teachers;

SELECT name
FROM students
UNION
SELECT name
FROM teachers;