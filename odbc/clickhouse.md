ODBC
sudo apt install openssl libicu unixodbc

iODBC
sudo apt install openssl libicu libiodbc2



wget "https://github.com/ClickHouse/clickhouse-odbc/releases/download/v1.1.4.20200302/clickhouse-odbc-1.1.4-Linux.tar.gz" 
tar xvzf clickhouse-odbc-1.1.4-Linux.tar.gz
cp clickhouse-odbc-1.1.4-Linux/lib64/*.so /usr/local/lib/
odbcinst -i -d -f clickhouse-odbc-1.1.4-Linux/share/doc/clickhouse-odbc/config/odbcinst.ini.sample
odbcinst -i -s -l -f clickhouse-odbc-1.1.4-Linux/share/doc/clickhouse-odbc/config/odbc.ini.sample
