FROM python:3.6
ADD . /myapp
WORKDIR /myapp
RUN pip3 install -r requirements.txt
CMD ["flask", "run", "--host", "0.0.0.0"]