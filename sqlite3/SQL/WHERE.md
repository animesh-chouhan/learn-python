# SQLite WHERE clause

The WHERE clause is an optional clause of the SELECT statement.

Besides the SELECT statement, you can use the WHERE clause in the UPDATE and DELETE statements.

It appears after the FROM clause as the following statement:

```sql
SELECT
    column_list
FROM
    table
WHERE
    search_condition;
```

The search condition in the WHERE has the following form:

```sql
left_expression COMPARISON_OPERATOR right_expression
```

Examples:

```sql
WHERE column_1 = 100;

WHERE column_2 IN (1,2,3);

WHERE column_3 LIKE 'An%';

WHERE column_4 BETWEEN 10 AND 20;
```

### =, !=, <,>,<=,>= Operators

When you compare two values, you must ensure that they are the same data type. You should compare numbers with numbers, string with strings, etc.

```sql
SELECT
   name,
   milliseconds,
   bytes,
   albumid
FROM
   tracks
WHERE
   albumid = 1
LIMIT 10;
```

### SQLite logical operators: ALL, AND, ANY, BETWEEN, EXISTS, IN, LIKE, NOT, OR

#### AND

```sql
SELECT
    name,
    milliseconds,
    bytes,
    albumid
FROM
    tracks
WHERE
    albumid = 1
AND milliseconds > 250000
LIMIT 10;
```

#### LIKE

```sql
SELECT
    name,
    albumid,
    composer
FROM
    tracks
WHERE
    composer LIKE '%Smith%'
ORDER BY
    albumid
LIMIT 10;
```

#### IN

```sql
SELECT
    name,
    albumid,
    mediatypeid
FROM
    tracks
WHERE
    mediatypeid IN (2,3)
LIMIT 10;
```
