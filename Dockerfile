FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code first
COPY src/ /app/src
COPY data/ /app/data
COPY setup.py .

# Then install the package in editable mode
RUN pip install -e .

EXPOSE 9999

HEALTHCHECK CMD curl --fail http://localhost:9999/_stcore/health

# Keep the working directory as /app (not /app/src)
# This allows the Python module imports to work correctly

ENTRYPOINT ["streamlit", "run", "src/Home.py", "--server.port=9999", "--server.address=0.0.0.0"]