# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

ARG PYTHON_VERSION=3.8.7
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1



# Switch to the appuser and set the working directory
WORKDIR /app

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser --disabled-password --gecos "" --no-create-home --shell "/sbin/nologin" --uid "${UID}" appuser

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip


# Switch to the non-privileged user to run the application.
USER appuser
# Create a writable directory for the user
RUN sudo mkdir /app/user-data && chown -R appuser:appuser /app/user-data
# Copy the source code into the container.
COPY MainScores.py .
COPY templates ./templates/
COPY requirements.txt .
COPY Scores.txt .
COPY requirements.txt /app/requirements.txt
# Install requirements
RUN python -m pip install -r /app/requirements.txt

# Expose the port that the application listens on.
EXPOSE 5000

# Run the application.
CMD python MainScores.py run --host=0.0.0.0 --port=5000
