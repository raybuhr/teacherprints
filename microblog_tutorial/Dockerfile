FROM conda/miniconda3

RUN apt-get update -y && apt-get install -y build-essential

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0"]
