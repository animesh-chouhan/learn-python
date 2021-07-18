# SQLite3

[SQLite Tutorial](https://www.sqlitetutorial.net/sqlite-commands/)

### Connect to an SQLite database

```sqlite3 ./db/chinook.db
.open ./db/chinook.db # after opening sqlite3
```

### Help

`.Help`

### Show databases

`.database`

### Adding additional database

`ATTACH DATABASE "./db/chinook.db" AS chinook`
Run .database again to see databases

### Exit

`.quit`

### Show tables in a database

`.tables`

#### See individual table with pattern matching

`.table "%es"`

### Show the structure of a table: Shows how the table was created

`.schema albums`

#### List schema of all tables

`.schema`

### Show indexes

`.indexes`

#### Show indexes of a table or use a pattern

```
.indexes albums
.indexes "%es"
```

### Save the result of a query in a file

To save the result of a query into a file, you use the .output FILENAME command. Once you issue the .output command, all the results of the subsequent queries will be saved to the file that you specified in the FILENAME argument. If you want to save the result of the next single query only to the file, you issue the .once FILENAME command.

To display the result of the query to the standard output again, you issue the .output command without arguments.

```
.output output.txt
SELECT title FROM albums
```

### Executing SQL statements from file

Suppose we have a file named commands.txt:

```
SELECT albumid, title
FROM albums
ORDER BY title
LIMIT 10;
```

```
.mode column
.header on
.read "commands.txt"
```
