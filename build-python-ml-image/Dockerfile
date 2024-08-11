FROM python:3.10-slim


RUN pip install --upgrade pip setuptools wheel

RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

RUN pip install transformers \
    fastapi \
    uvicorn[standard] 


WORKDIR /app

CMD ["python"]