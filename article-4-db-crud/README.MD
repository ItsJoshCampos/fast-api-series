# Article 4 - SQL Server DB Connection

This article will walkthrough setting up a SQL Server Db connection from your FastAPI.  We'll reuse some of the code from article-2-env-file project.  Some minimal changes to restructure the reading of ENV variables in FastAPI while utilizing LRU Caching.

SQL Alchemy will be used as an ORM when reading and writing to our SQL Server Db. 

SQL Server can be used on both Windows and *nix OSs.  Follow the guide this [blog post](https://itsjoshcampos.codes/run-sql-server-on-macos-docker) to get SQL Server setup on macOS.

## Local Setup for Dev

From this project directory, follow the steps:

### 1. Setup Virtual Environment
You should already have `virtualenv` already installed.
Create a virtual environment with the command below. Consider using `venv` as the name since its already added to the .gitignore file. 

```bash
python3 -m venv venv
```

### 2. Activate your Virtual Environment

```bash
source venv/bin/activate
```

### 3. Install FastAPI Directly
```bash
pip install "FastAPI[all]"
 ```

### 4. Startup FASTApi Server
```bash
uvicorn app:app --reload
 ```

## Swagger Doc
Built-in Swagger Documentation is available at: `http://localhost:8000/docs`

## SQL Server
If you already have a SQL Server Db, just run the `DB_Scripts/SEED_Script.sq`l file to create a new table and insert a row of data to start using in your API. 