use library_pr;

/*CREATE TABLE user(
    user_id INT AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL unique,
    pswd VARCHAR(50) NOT NULL,
    gender CHAR(1),
    noof_current_books INT default 0,
    n_read int default 0,
    pic BLOB,
    PRIMARY KEY (user_id)
);
create table emp(
   e_id int auto_increment,
   name VARCHAR(20) NOT NULL,
   email VARCHAR(50) NOT NULL unique,
   pswd VARCHAR(50) NOT NULL,
   gender CHAR(1),
   salary int,
   primary key (e_id)
);

CREATE TABLE books(
   book_id INT AUTO_INCREMENT,
   genre VARCHAR(20) NOT NULL DEFAULT 'other',
   name VARCHAR(100) NOT NULL,
   authors VARCHAR(100) NOT NULL,
   publi_date DATE,
   n_copies INT,
   available INT,
   n-read INT default 0;
   description TEXT,
   cover BLOB,
   PRIMARY KEY (book_id)
);
CREATE TABLE comments(
   book_id INT,
   user_id INT,
   comment TEXT,
   PRIMARY KEY(book_id, user_id),
   FOREIGN KEY(book_id) REFERENCES books(book_id) ON DELETE CASCADE,
   FOREIGN KEY(user_id) REFERENCES user(user_id) ON DELETE CASCADE
);

CREATE TABLE orders(
    order_id INT AUTO_INCREMENT,
    book_id INT,
    user_id INT,
    taken DATETIME DEFAULT CURRENT_TIMESTAMP,
    exp_return DATETIME DEFAULT (DATE_ADD(current_timestamp(), INTERVAL 10 DAY)),
    r_status varchar(8) DEFAULT 'using',
    PRIMARY KEY(order_id),
    FOREIGN KEY(book_id) REFERENCES books(book_id) ON DELETE SET NULL,
    FOREIGN KEY(user_id) REFERENCES user(user_id) ON DELETE SET NULL
);*/
-- user registering into data base
/*INSERT INTO USER (name, email, pswd, gender)
VALUES ('', '@gmail.com', MD5(''), '');*/
/*insert into emp(name,email,pswd,gender,salary)
values ('sitara','sita@gmail.com',MD5('s123'),'m',40000);*/

/*-- ading books
INSERT INTO books (genre, name, authors, publi_date, n_copies, available, description, cover)
values ('Computer science', 'An Introduction to Statistical Learning: With Applications in R',"Gareth James, Trevor Hastie, Robert Tibshirani, Daniela Witten",
'2017-01-26','6','6',"provides an accessible overview of the field of statistical learning, an essential toolset for making sense of the vast and complex data sets that have emerged in fields ranging from biology to finance to marketing to astrophysics in the past twenty years. This book presents some of the most important modeling and prediction techniques, along with relevant applications. Topics include linear regression, classification, resampling methods, shrinkage approaches, tree-based methods, support vector machines, clustering, and more. Color graphics and real-world examples are used to illustrate the methods presented"
,LOAD_FILE(''));

INSERT INTO books (genre, name, authors, publi_date, n_copies, available, description, cover)
values ('physics','The Feynman Lectures on Physics Vol 1', 'Richard P. Feynman, Robert B. Leighton, Matthew L. Sands', "2005-09-01",4,4,
'published in 1963, the three-volume Feynman lectures on physics set remains a classic text Originally. This edition, which was prepared by Kip S. Thorne (Feynman Professor of Theoretical Physics at California Institute of Technology), fully incorporates all the errata and corrections gathered (but never used in a published edition) by Feynman.',
load_file(''));
*/
/* trigger to update user books and available books when ordered
delimiter $$
create trigger book_order
after insert on orders for each row
begin 
  declare aval int;
  select available into aval from books where book_id = new.book_id;
 if  aval > 0 then
  update user
    set user.noof_current_books=user.noof_current_books+1
     where user.user_id = new.user_id;
  update books 
   set books.available = books.available -1
   where books.book_id = new.book_id;
   end if;
end $$
delimiter ;
*/
/*
to update available books and user books when user returned 
delimiter $$
create trigger book_return
after update on orders for each row 
begin 
declare cb int;
select noof_current_books into cb from user where user_id = new.user_id;
if cb > 0  and new.r_status = 'returned' then 
 update user
 set user.noof_current_books = user.noof_current_books -1, user.n_read = user.n_read+1
 where user.user_id = new.user_id;
 update books 
   set books.available = books.available +1,books.n_read = books.n_read + 1
   where books.book_id = new.book_id;
   end if;
end $$
delimiter ;

*/
/*
--  user ordering a book 
insert into orders(book_id,user_id)
values (,);
select * from orders;
-- a user is returning a book
update orders 
set r_status = 'returned', exp_return =  now()
where order_id = ; 
*/
/*
-- user comments on a book 
insert into comments
values(2,3,'It is a very good book to learn how to handle large data sets');
*/
/*-- user searched by genre 
select * from books 
where genre = ''; --use the genre inthe quotes
*/

/* --user specified name of book
select * from books 
where locate('',name)>0;  -- use word to search in the quotes 
*/









