FROM python:3.9 AS base
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM base AS final
COPY --from=base /app /app
COPY . .

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app --worker-class uvicorn.workers.UvicornWorker