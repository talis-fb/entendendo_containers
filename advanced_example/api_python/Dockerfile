FROM python:3.9

# Aqui ele seta o pasta "atual" do container
# Ou seja, não é necessário usar 'cd /usr/app' toda vez
# e na linha 14 o backend/ da direita é na verdade '/usr/app/backend/'
WORKDIR /usr/app

RUN pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --system --deploy

COPY backend/ backend/

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8080"]
