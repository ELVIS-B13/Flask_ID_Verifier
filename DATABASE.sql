-- Create the table
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    id_number TEXT NOT NULL,
    year_of_start INTEGER NOT NULL,
    year_of_graduation INTEGER NOT NULL
);

-- Insert data into the table
INSERT INTO students (name, id_number, year_of_start, year_of_graduation) VALUES
    ('REUBEN', '001', 2021, 2022),
    ('ASAD', '002', 2021, 2022),
    ('SHALEM', '003', 2021, 2022),
    ('DINAKER', '004', 2021, 2022);

SELECT * FROM students;
