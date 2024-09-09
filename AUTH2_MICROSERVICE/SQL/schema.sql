CREATE DATABASE IF NOT EXISTS auth2;
USE auth2;

DROP TABLE IF EXISTS contacts;
DROP TABLE IF EXISTS addresses;
DROP TABLE IF EXISTS permissions_roles;
DROP TABLE IF EXISTS users_roles;
DROP TABLE IF EXISTS permissions;
DROP TABLE IF EXISTS roles;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS authentications;

CREATE TABLE `roles` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `role` VARCHAR(80) NOT NULL ,
  `enabled` TINYINT NOT NULL DEFAULT '1'
);

CREATE TABLE `permissions` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `permission` VARCHAR(80) NOT NULL UNIQUE,
  `enabled` TINYINT NOT NULL DEFAULT '1',
  `resource_path` VARCHAR(1023) DEFAULT NULL,
  `access_type` VARCHAR(255) DEFAULT NULL,
  `note` VARCHAR(255) DEFAULT NULL
);

CREATE TABLE `permissions_roles` (
  `permission_id` BIGINT(20) NOT NULL,
  `role_id` BIGINT(20) NOT NULL,
  PRIMARY KEY (permission_id, role_id),
  FOREIGN KEY (permission_id) REFERENCES permissions(id),
  FOREIGN KEY (role_id) REFERENCES roles(id)
);

CREATE TABLE `users` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `username` VARCHAR(100) NOT NULL UNIQUE,
  `password` VARCHAR(255) NOT NULL,
  `name` VARCHAR(100) DEFAULT NULL,
  `surname` VARCHAR(100) DEFAULT NULL,
  `gender` VARCHAR(1) DEFAULT NULL,
  `birth_date` DATE DEFAULT NULL,
  `enabled` TINYINT NOT NULL DEFAULT '1',
  `creation_dt` TIMESTAMP NOT NULL DEFAULT current_TIMESTAMP,
  `updated_dt` TIMESTAMP DEFAULT current_TIMESTAMP,
  `login_dt` TIMESTAMP DEFAULT NULL,
  `note` VARCHAR(255) DEFAULT NULL,
  `secured` TINYINT NOT NULL DEFAULT '0'
);

CREATE TABLE `users_roles` (
  `user_id` BIGINT(20) NOT NULL,
  `role_id` BIGINT(20) NOT NULL,
  PRIMARY KEY (user_id, role_id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (role_id) REFERENCES roles(id)
);

CREATE TABLE `users_permissions` (
  `user_id` BIGINT(20) NOT NULL,
  `permission_id` BIGINT(20) NOT NULL,
  PRIMARY KEY (user_id, permission_id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (permission_id) REFERENCES permissions(id)
);

CREATE TABLE `contacts` (
  `user_id` BIGINT(20) NOT NULL PRIMARY KEY,
  `email` VARCHAR(255) NOT NULL UNIQUE,
  `phone` VARCHAR(20) DEFAULT NULL,
  `skype` VARCHAR(255) DEFAULT NULL,
  `facebook` VARCHAR(255) DEFAULT NULL,
  `linkedin` VARCHAR(255) DEFAULT NULL,
  `website` VARCHAR(255) DEFAULT NULL,
  `note` VARCHAR(255) DEFAULT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE `addresses` (
  `user_id` BIGINT(20) NOT NULL PRIMARY KEY,
  `address` VARCHAR(255) DEFAULT NULL,
  `address2` VARCHAR(255) DEFAULT NULL,
  `city` VARCHAR(20) DEFAULT NULL,
  `country` VARCHAR(20) DEFAULT NULL,
  `zip_code` VARCHAR(20) DEFAULT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE `authentications` (
  `user_id` BIGINT(20) NOT NULL,
  `auth_token` VARCHAR(255) NOT NULL UNIQUE,
  `creation_dt` TIMESTAMP NOT NULL DEFAULT current_TIMESTAMP,
  `duration` BIGINT(20) NOT NULL DEFAULT 3600,
  PRIMARY KEY (user_id, auth_token),
  FOREIGN KEY (user_id) REFERENCES users(id)
);