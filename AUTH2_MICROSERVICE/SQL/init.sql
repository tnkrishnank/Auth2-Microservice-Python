GRANT ALL PRIVILEGES ON *.* TO `root`@`%`;
FLUSH PRIVILEGES;
SOURCE /app/schema.sql;
SOURCE /app/data.sql;