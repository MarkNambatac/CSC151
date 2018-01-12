RDBMS used: PostreSQL

Database named students was created using PgAdmin 4 v2.0 
Screenshots included in the other folder named Screenshots

(Please Refer to Picture No. 1)

We can always use the SQL Command in the SQL shell or insert in in your python code.

CREATE TABLE students (
    id_no text NOT NULL UNIQUE,
    name text NOT NULL UNIQUE,
    course text NOT NULL UNIQUE
);

This command will create a Unique constraint on the "id_no", "name", and "course" column when students table is created
In order also to not let the user enter multiple entries in the database

In PgAdmin please refer to Picture No 2 on how to create a unique constraint on the columns.
