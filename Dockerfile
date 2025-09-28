FROM python:3.14.0rc3-alpine3.22

# Install uv
RUN pip install --no-cache-dir --upgrade pip && \
pip install --no-cache-dir uv

# Copy the dora directory into the container
# Set working directory
COPY . /dora
WORKDIR /dora

# Install dependencies using uv
RUN uv sync

# Set the entry point to run the dora.ui.app module
ENTRYPOINT ["python", "-m", "dora.ui.app"]