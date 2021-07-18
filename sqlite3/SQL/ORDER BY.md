# ORDER BY

### SQLite ORDER BY clause

```sql
SELECT
   select_list
FROM
   table
ORDER BY
    column_1 ASC,
    column_2 DESC;
```

```sql
SELECT
    name,
    milliseconds,
    albumid
FROM
    tracks
ORDER BY
    albumid ASC,
    milliseconds DESC
LIMIT 10;
```

### SQLite ORDER BY with the column position

For example, the following statement sorts the tracks by both albumid (3rd column) and milliseconds (2nd column) in ascending order.

```sql
SELECT
    name,
    milliseconds,
    albumid
FROM
    tracks
ORDER BY
     3,2
LIMIT 10;
```

### Sorting NULLs

NULL is special because you cannot compare it with another value. Simply put, if the two pieces of information are unknown, you cannot compare them.

NULL is even cannot be compared with itself; NULL is not equal to itself so NULL = NULL always results in false.

When it comes to sorting, SQLite considers NULL to be smaller than any other value.

It means that NULLs will appear at the beginning of the result set if you use ASC or at the end of the result set when you use DESC.

SQLite 3.30.0 added the NULLS FIRST and NULLS LAST options to the ORDER BY clause. The NULLS FIRST option specifies that the NULLs will appear at the beginning of the result set while the NULLS LAST option place NULLs at the end of the result set.

```sql
SELECT
    TrackId,
    Name,
    Composer
FROM
    tracks
ORDER BY
    Composer
    NULLS LAST
LIMIT 10;
```
