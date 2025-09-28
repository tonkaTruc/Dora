FROM python:3.14.0rc3-alpine3.22

# Set working directory
WORKDIR /app

# Copy the dora directory into the container
COPY . /app/dora

# Install uv
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir uv

# Install dependencies using uv
RUN uv sync /app/dora/pyproject.toml

# Set the entry point to run the dora.ui.app module
ENTRYPOINT ["python", "-m", "dora.ui.app"]