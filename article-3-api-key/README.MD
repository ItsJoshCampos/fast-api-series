# Article 3 - API Keys

This article will walkthrough setting up an API Key.  We'll reuse some of the code from article-2-env-file project.  Some minimal changes to restructure the reading of ENV variables in FastAPI while utilizing LRU Caching.  

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