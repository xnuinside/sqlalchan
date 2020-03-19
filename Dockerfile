FROM python:3.7.4
COPY pyproject.toml /main/pyproject.toml
RUN pip install --upgrade pip
WORKDIR /main
COPY sqlalchan /main/sqlalchan
RUN pip install .
ENV PYTHONPATH = $PYTHONPATH:/main/
