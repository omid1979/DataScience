CREATE DATABASE IF NOT EXISTS mydb001;


CREATE USER omid IDENTIFIED WITH sha256_password BY ‘pass';



CREATE ROLE 'admin';
GRANT ALL ON *.* TO admin WITH GRANT OPTION;

create user test identified with plaintext_password by 'test';
GRANT admin to test;


SELECT
    floor(randNormal(100, 5)) AS k,
    count(*) AS c,
    bar(c, 0, 50000, 100)
FROM numbers(100000) GROUP BY k ORDER BY k ASC



######### Sample Data1

CREATE TABLE purchases
(
    `dt` DateTime,
    `customer_id` UInt32,
    `total_spent` Float32
)
ENGINE = MergeTree
ORDER BY dt


INSERT INTO purchases SELECT
    now() - randUniform(1, 1000000.),
    number,
    15 + round(randExponential(1 / 10), 2)
FROM numbers(1000000)

i########## Sampel Data2

CREATE TABLE events
(
    `dt` DateTime,
    `event` String
)
ENGINE = MergeTree
ORDER BY dt



INSERT INTO events SELECT
    toDateTime('2022-12-12 12:00:00') - (((12 + randPoisson(12)) * 60) * 60),
    'click'
FROM numbers(100000)




## config.xml

<clickhouse>
    <password_complexity>
        <rule>
            <pattern>.{12}</pattern>
            <message>be at least 12 characters long</message>
        </rule>
        <rule>
            <pattern>\p{N}</pattern>
            <message>contain at least 1 numeric character</message>
        </rule>
    </password_complexity>
</clickhouse>




