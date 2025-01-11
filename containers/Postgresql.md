

Regrence :  https://blog.cadumagalhaes.dev/how-to-setup-a-postgresql-database-with-docker-compose


Postgre15 with pgAdmin

###############################################################################################

Enable Remote Connection : 

postgresql.conf   => 
	listen_addresses = '*'

pg_hba.conf       => 
	host    all             all              0.0.0.0/0                       md5


sudo -u postgres psql
postgres=# create database mydb;
postgres=# create user omid with encrypted password 'cluster';
postgres=# grant all privileges on database mydb to omid;

$ sudo -u postgres createuser <username>
$ sudo -u postgres createdb <dbname>

$ sudo -u postgres psql
psql=# alter user <username> with encrypted password '<password>';

psql=# grant all privileges on database <dbname> to <username> ;







sudo -u postgres createuser --interactive


List Users : 
\du


