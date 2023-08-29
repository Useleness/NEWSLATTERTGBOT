# How tf should I use this?
- Start main.py
> Yep, thats all😅

## How could I create my database.db?
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

## Why bot is not working?
> Probably you dont have telegram python module, try to use this in your cmd:
```
py -m pip install aiogram -U
```
> If you dont have [Python](https://www.python.org/downloads/) installed on ur PC, then install it and try again