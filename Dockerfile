FROM python
WORKDIR /solar-system


COPY . .

RUN pip install -r requirements.txt

CMD python __main__.py
