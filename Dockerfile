FROM python
WORKDIR /app
RUN pip install flask
ENV VERSION=1.0.0
COPY . /app
CMD python app.py
