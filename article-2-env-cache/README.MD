# Article 2 - Environment Variables with LRU Caching

This article will walkthrough reading in ENV variables in FastAPI utilizing LRU Caching.  

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
API_KEY="SECRETKEY" APP_MAX="799" uvicorn app:app --reload
 ```

## Swagger Doc
Built-in Swagger Documentation is available at: `http://localhost:8000/docs`