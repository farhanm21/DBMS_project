
CREATE TABLE issued_book (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES student(id),
    book_id INTEGER REFERENCES home_book(id),
    issue_date DATE DEFAULT CURRENT_DATE,
    return_date DATE
);
--To ensure Table is in 3NF--
ALTER TABLE issued_book
ADD CONSTRAINT fk_student
FOREIGN KEY (student_id)
REFERENCES Student(ID);

ALTER TABLE issued_book
ADD CONSTRAINT fk_book
FOREIGN KEY (book_id)
REFERENCES home_book(id);

--Issuing books to students--
INSERT INTO issued_book (student_id, book_id, issue_date, return_date)
VALUES (1, 1, '2024-05-10', '2024-06-10');

--Shows detail of book issued by student--
SELECT b.title, b.author, b.isbn, b.genre, s.username AS student_name
FROM issued_book ib
JOIN home_book b ON ib.book_id = b.id
JOIN student s ON ib.student_id = s.id;

--Shows number of Books issued by each Student--
SELECT s.ID AS student_id, s.USERNAME AS student_username, COUNT(ib.id) AS issued_books_count
FROM Student s
LEFT JOIN issued_book ib ON s.ID = ib.student_id
GROUP BY s.ID, s.USERNAME;




--This table has been generetated using django model--
CREATE Table Student(
    ID INT PRIMARY KEY,
    USERNAME VARCHAR(50) UNIQUE,
    PASSWORD VARCHAR(128),
    EMAIL VARCHAR(112) UNIQUE
);


--Sample Querie to insert into book--
insert into home_book(title, isbn, genre,author) values ('Matilda', '7','Fiction','Roald dahl');


--This table has been generated using django model--
CREATE TABLE home_book(
ID INT PRIMARY KEY,
TITLE VARCHAR(100),
AUTHOR VARCHAR(100),
ISBN VARCHAR(20),
GENRE VARCHAR(20)
);

--Trigger Function to insert into issued_book table--
CREATE OR REPLACE FUNCTION insert_issued_book_trigger_function()
RETURNS TRIGGER AS $$
BEGIN
    -- Insert the new book into the issued_book table
    INSERT INTO issued_book (student_id, book_id, issue_date)
    VALUES (NEW.student_id, NEW.id, CURRENT_DATE);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create the trigger
CREATE TRIGGER insert_issued_book_trigger
AFTER INSERT ON home_book
FOR EACH ROW
EXECUTE FUNCTION insert_issued_book_trigger_function();