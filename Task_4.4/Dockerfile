# --- Task 4.4 (High Distinction) Dockerfile ---
# Best-practice notes for the report:
#  - slim base image to minimize footprint
#  - non-root user for security
#  - no exposed ports (this is a non-web, task-based container)
#  - designed to be run with -v for host/volume mounts, not baked-in data

FROM python:3.12-slim

WORKDIR /app

COPY process_data.py .

# Create and switch to a non-root user (Docker best practice)
RUN useradd -m clitool
USER clitool

# The container expects /app/data to be provided via -v at runtime
ENTRYPOINT ["python", "process_data.py"]
