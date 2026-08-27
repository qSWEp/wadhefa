# Database Schema

## jobs 

```sql
CREATE TABLE jobs (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    url TEXT UNIQUE,
    status TEXT DEFAULT 'saved' CHECK (status IN ('saved', 'applied', 'rejected'))

);
```