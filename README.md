# How could I create my database.db?
1. Start main.py
2. After initialization press: CTRL+C
3. Open db.db with [SQLiteStudio](https://sqlitestudio.pl/)
4. Create table "users"
5. Add column "id" - INTEGER, PRIMARY KEY, AUTOINCREMENT
6. Add column "user_id" - INTEGER, UNIQUE, NOT NULL
7. Add column "active" - INTEGER, DEFAULT (1)
8. Save it