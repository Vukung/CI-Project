# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /code

# Copy the requirements.txt file into the container at /code/requirements.txt
COPY ./requirements.txt /code/requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy your project files (including ML scripts, model files, etc.) into the container
COPY ./ /code/

# Expose the port your app will run on (adjust if necessary)
EXPOSE 8000

# Command to run the ML model or FastAPI app
# Replace `app.server:app` with the path to your FastAPI app or script if needed
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]


# http://127.0.0.1:8000/
# http://localhost:8000/