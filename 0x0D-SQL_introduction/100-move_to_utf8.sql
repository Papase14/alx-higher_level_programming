-- converts hbtn_0c_0 database to UTF8
-- cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p 

USE hbtn_0c_0
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
