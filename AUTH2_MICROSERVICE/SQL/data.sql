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

INSERT INTO permissions(id, permission, note) VALUES (1, 'CREATE_USER', 'Create a new user');
INSERT INTO permissions(id, permission, note) VALUES (2, 'READ_USER', 'Read a user data');
INSERT INTO permissions(id, permission, note) VALUES (3, 'UPDATE_USER', 'Update a user data');
INSERT INTO permissions(id, permission, note) VALUES (4, 'DELETE_USER', 'Delete a user');
INSERT INTO permissions(id, permission, note) VALUES (5, 'ADD_PERMISSION_USER', 'Add permission on a user');
INSERT INTO permissions(id, permission, note) VALUES (6, 'DELETE_PERMISSION_USER', 'Delete permission on a user');
INSERT INTO permissions(id, permission, note) VALUES (7, 'ADD_ROLE_USER', 'Add role on a user');
INSERT INTO permissions(id, permission, note) VALUES (8, 'DELETE_ROLE_USER', 'Delete role on a user');
INSERT INTO permissions(id, permission, note) VALUES (9, 'CREATE_ROLE', 'Create a new role');
INSERT INTO permissions(id, permission, note) VALUES (10, 'READ_ROLE', 'Read a role data');
INSERT INTO permissions(id, permission, note) VALUES (11, 'UPDATE_ROLE', 'Update a role data');
INSERT INTO permissions(id, permission, note) VALUES (12, 'DELETE_ROLE', 'Delete a role');
INSERT INTO permissions(id, permission, note) VALUES (13, 'CREATE_PERMISSION', 'Create a new permission');
INSERT INTO permissions(id, permission, note) VALUES (14, 'READ_PERMISSION', 'Read a permission data');
INSERT INTO permissions(id, permission, note) VALUES (15, 'UPDATE_PERMISSION', 'Update a permission data');
INSERT INTO permissions(id, permission, note) VALUES (16, 'DELETE_PERMISSION', 'Delete a permission');
INSERT INTO permissions(id, permission, note) VALUES (17, 'ADD_PERMISSION_ROLE', 'Add permission on a role');
INSERT INTO permissions(id, permission, note) VALUES (18, 'DELETE_PERMISSION_ROLE', 'Delete permission on a role');

INSERT INTO roles(id, role) VALUES (1, 'ADMINISTRATOR');
INSERT INTO roles(id, role) VALUES (2, 'MANAGER');
INSERT INTO roles(id, role) VALUES (3, 'TEAM_LEAD');

INSERT INTO permissions_roles(permission_id, role_id) VALUES (1, 1);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (2, 1);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (3, 1);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (4, 1);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (9, 2);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (10, 2);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (11, 2);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (12, 2);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (13, 2);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (14, 2);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (15, 2);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (16, 2);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (17, 2);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (18, 2);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (2, 3);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (10, 3);
INSERT INTO permissions_roles(permission_id, role_id) VALUES (14, 3);

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
INSERT INTO users_roles(user_id, role_id) VALUES (2, 2);
INSERT INTO users_roles(user_id, role_id) VALUES (3, 2);
INSERT INTO users_roles(user_id, role_id) VALUES (4, 3);
INSERT INTO users_roles(user_id, role_id) VALUES (5, 3);
INSERT INTO users_roles(user_id, role_id) VALUES (6, 3);

INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 1);
INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 2);
INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 3);
INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 4);
INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 5);
INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 6);
INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 7);
INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 8);
INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 9);
INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 10);
INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 11);
INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 12);
INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 13);
INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 14);
INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 15);
INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 16);
INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 17);
INSERT INTO users_permissions(user_id, permission_id) VALUES (7, 18);
INSERT INTO users_permissions(user_id, permission_id) VALUES (8, 2);