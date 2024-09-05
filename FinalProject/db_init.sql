-- create the user
CREATE USER "ShopieDB_Admin" WITH PASSWORD 'ShopieDB_Admin_pwd';

-- create the database
CREATE DATABASE "ShopieDB";

-- connect to the shopiedb database as a superuser (e.g., postgres)
\c "ShopieDB"

-- grant all privileges on the database to ShopieDB_Admin
GRANT ALL PRIVILEGES ON DATABASE "ShopieDB" TO "ShopieDB_Admin";

-- grant usage and create privileges on the public schema
GRANT USAGE, CREATE ON SCHEMA public TO "ShopieDB_Admin";

-- grant all privileges on all tables in the public schema
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO "ShopieDB_Admin";

-- grant all privileges on all sequences in the public schema
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO "ShopieDB_Admin";

-- make ShopieDB_Admin the owner of the public schema
ALTER SCHEMA public OWNER TO "ShopieDB_Admin";

-- make future tables to be owned by ShopieDB_Admin by default:
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON TABLES TO "ShopieDB_Admin";
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL PRIVILEGES ON SEQUENCES TO "ShopieDB_Admin";