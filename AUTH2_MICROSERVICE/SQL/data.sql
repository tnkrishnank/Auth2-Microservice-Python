USE auth2;

DELETE FROM permissions_roles;
DELETE FROM users_permissions;
DELETE FROM permissions;
DELETE FROM users_roles;
DELETE FROM roles;
DELETE FROM contacts;
DELETE FROM addresses;
DELETE FROM authentications;
DELETE FROM users;

INSERT INTO permissions(id, permission, note) VALUES (1, 'MANAGE_USER_DATA', 'Manage User Data');
INSERT INTO permissions(id, permission, resource_path, access_type, note) VALUES (2, 'MANAGER_DRIVE_EDIT', 'MANAGER', 'EDIT', 'Manager Directory Edit');
INSERT INTO permissions(id, permission, resource_path, access_type, note) VALUES (3, 'MANAGER_DRIVE_VIEW', 'MANAGER', 'VIEW', 'Manager Directory Edit');
INSERT INTO permissions(id, permission, resource_path, access_type, note) VALUES (4, 'PROJECT_FILES_EDIT', 'PROJECT', 'EDIT', 'Project Files Directory Edit');
INSERT INTO permissions(id, permission, resource_path, access_type, note) VALUES (5, 'PROJECT_FILES_VIEW', 'PROJECT', 'VIEW', 'Project Files Directory View');

INSERT INTO roles(id, role) VALUES (1, 'ADMINISTRATOR');
INSERT INTO roles(id, role) VALUES (2, 'MANAGER');
INSERT INTO roles(id, role) VALUES (3, 'TEAM_LEAD');

INSERT INTO permissions_roles(permission_id, role_id) VALUES (1, 1);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (2, 2);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (4, 2);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (3, 3);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (4, 3);

INSERT INTO users(id, username, password, name, surname, gender, birth_date) VALUES (1, 'test1', '99f2bdf9942653ab32d9dfa0b43c72c3fbbb9679450fd965c590c224897b848a', 'Alex', 'Ivan', 'M', '1978-01-08');
INSERT INTO users(id, username, password, name, surname, gender, birth_date) VALUES (2, 'test2', '99f2bdf9942653ab32d9dfa0b43c72c3fbbb9679450fd965c590c224897b848a', 'Brad', 'Jack', 'F', '1980-02-11');
INSERT INTO users(id, username, password, name, surname, gender, birth_date) VALUES (3, 'test3', '99f2bdf9942653ab32d9dfa0b43c72c3fbbb9679450fd965c590c224897b848a', 'Carl', 'Kyle', 'M', '1982-03-14');
INSERT INTO users(id, username, password, name, surname, gender, birth_date) VALUES (4, 'test4', '99f2bdf9942653ab32d9dfa0b43c72c3fbbb9679450fd965c590c224897b848a', 'Drew', 'Luke', 'F', '1984-04-17');
INSERT INTO users(id, username, password, name, surname, gender, birth_date) VALUES (5, 'test5', '99f2bdf9942653ab32d9dfa0b43c72c3fbbb9679450fd965c590c224897b848a', 'Eric', 'Mark', 'M', '1986-05-20');
INSERT INTO users(id, username, password, name, surname, gender, birth_date) VALUES (6, 'test6', '99f2bdf9942653ab32d9dfa0b43c72c3fbbb9679450fd965c590c224897b848a', 'Finn', 'Noah', 'F', '1988-06-23');
INSERT INTO users(id, username, password, name, surname, gender, birth_date) VALUES (7, 'test7', '99f2bdf9942653ab32d9dfa0b43c72c3fbbb9679450fd965c590c224897b848a', 'Gary', 'Omer', 'M', '1990-07-26');
INSERT INTO users(id, username, password, name, surname, gender, birth_date) VALUES (8, 'test8', '99f2bdf9942653ab32d9dfa0b43c72c3fbbb9679450fd965c590c224897b848a', 'Hank', 'Paul', 'F', '1992-08-29');

INSERT INTO contacts(user_id, email, phone) VALUES (1, 'alex@gmail.com', '9876543211');
INSERT INTO contacts(user_id, email, phone) VALUES (2, 'brad@gmail.com', '9876543212');
INSERT INTO contacts(user_id, email, phone) VALUES (3, 'carl@gmail.com', '9876543213');
INSERT INTO contacts(user_id, email, phone) VALUES (4, 'drew@gmail.com', '9876543214');
INSERT INTO contacts(user_id, email, phone) VALUES (5, 'eric@gmail.com', '9876543215');
INSERT INTO contacts(user_id, email, phone) VALUES (6, 'finn@gmail.com', '9876543216');
INSERT INTO contacts(user_id, email, phone) VALUES (7, 'gary@gmail.com', '9876543217');
INSERT INTO contacts(user_id, email, phone) VALUES (8, 'hank@gmail.com', '9876543218');

INSERT INTO addresses(user_id, address, address2, city, country, zip_code) VALUES (1, 'addr1', 'addr2', 'Florida', 'US', '34787');
INSERT INTO addresses(user_id, address, address2, city, country, zip_code) VALUES (2, 'addr1', 'addr2', 'Florida', 'US', '34787');
INSERT INTO addresses(user_id, address, address2, city, country, zip_code) VALUES (3, 'addr1', 'addr2', 'Florida', 'US', '34787');
INSERT INTO addresses(user_id, address, address2, city, country, zip_code) VALUES (4, 'addr1', 'addr2', 'Florida', 'US', '34787');
INSERT INTO addresses(user_id, address, address2, city, country, zip_code) VALUES (5, 'addr1', 'addr2', 'Florida', 'US', '34787');
INSERT INTO addresses(user_id, address, address2, city, country, zip_code) VALUES (6, 'addr1', 'addr2', 'Florida', 'US', '34787');
INSERT INTO addresses(user_id, address, address2, city, country, zip_code) VALUES (7, 'addr1', 'addr2', 'Florida', 'US', '34787');
INSERT INTO addresses(user_id, address, address2, city, country, zip_code) VALUES (8, 'addr1', 'addr2', 'Florida', 'US', '34787');

UPDATE users SET secured = true WHERE id = 1;
UPDATE users SET enabled = false WHERE id = 8;

INSERT INTO users_roles(user_id, role_id) VALUES (1, 1);
INSERT INTO users_roles(user_id, role_id) VALUES (1, 2);
INSERT INTO users_roles(user_id, role_id) VALUES (2, 2);
INSERT INTO users_roles(user_id, role_id) VALUES (3, 2);
INSERT INTO users_roles(user_id, role_id) VALUES (4, 3);
INSERT INTO users_roles(user_id, role_id) VALUES (5, 3);
INSERT INTO users_roles(user_id, role_id) VALUES (6, 3);

INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 5);
INSERT INTO users_permissions(user_id, permission_id) VALUES (8, 5);