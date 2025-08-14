# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container at /code
COPY ./requirements.txt /code/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the rest of the application's code into the container
COPY . /code/

# Make port 7860 available to the world outside this container
EXPOSE 7860

# --- THE FINAL FIX ---
# Run gunicorn as a Python module to avoid PATH issues
CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:7860", "app:app"]
