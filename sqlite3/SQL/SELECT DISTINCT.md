# SQLite Select Distinct

The DISTINCT clause is an optional clause of the SELECT statement. The DISTINCT clause allows you to remove the duplicate rows in the result set.

In this syntax:

- First, the DISTINCT clause must appear immediately after the SELECT keyword.

- Second, you place a column or a list of columns after the DISTINCT keyword. If you use one column, SQLite uses values in that column to evaluate the duplicate. In case you use multiple columns, SQLite uses the combination of values in these columns to evaluate the duplicate.

SQLite considers NULL values as duplicates. If you use the DISTINCT clause with a column that has NULL values, SQLite will keep one row of a NULL value.

```sql
SELECT DISTINCT city
FROM customers
ORDER BY city
LIMIT 10;
```

### SQLite SELECT DISTINCT on multiple columns

```sql
SELECT DISTINCT
    city,
    country
FROM
    customers
ORDER BY
    country
LIMIT 10;
```

### SQLite SELECT DISTINCT with NULL example

If you apply the DISTINCT clause to the statement, it will keep only one row with a NULL value.

```sql
SELECT DISTINCT company
FROM customers
LIMIT 10;
```
