# Use the standard Python 3.9 image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the working directory
COPY requirements.txt .

# Install the Python libraries specified in the requirements file
RUN pip install -r requirements.txt

# Copy all your other files (app.py, index.html) into the working directory
COPY . .

# Tell the container to listen on port 7860
EXPOSE 7860

# The command to run your application using gunicorn
CMD ["python", "-m", "gunicorn", "app:app", "--bind", "0.0.0.0:7860"]
