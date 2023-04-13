FROM python:3.9 AS base
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM base AS final
COPY --from=base /app /app
COPY . .

CMD ["python","-m", "uvicorn", "main:app", "--host", "0.0.0.0"]