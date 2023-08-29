# How could I create my database.db?
- Start main.py
- After initialization press: CTRL+C
- Open db.db with [SQLiteStudio](https://sqlitestudio.pl/)
- Create table "users"
- Add column "id" 
  - INTEGER, PRIMARY KEY, AUTOINCREMENT
- Add column "user_id" 
  - INTEGER, UNIQUE, NOT NULL
- Add column "active" 
  - INTEGER, DEFAULT (1)
- Save it
> Good luck!