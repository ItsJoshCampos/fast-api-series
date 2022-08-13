# Using Python 3.9 
FROM python:3.9

# Setup working directory
RUN mkdir code
WORKDIR /code

# Copy requirements file to our working directory
COPY ./requirements.txt /code/requirements.txt

# Install packages - Use cache dependencies 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./ /code/app

# 
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]
