# SELECT

[URL](https://www.sqlitetutorial.net/sqlite-select)

### Expression

```sql
SELECT 1 + 1;
SELECT  10 / 5;
```

### Querying data from a table

```sql
SELECT DISTINCT column_list
FROM table_list
  JOIN table ON join_condition
WHERE row_filter
ORDER BY column
LIMIT count OFFSET offset
GROUP BY column
HAVING group_filter;
```

```sql
SELECT trackid, name
FROM tracks
LIMIT 10
OFFSET 5;
```
