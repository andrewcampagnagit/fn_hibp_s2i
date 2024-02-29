FROM python:3.7.3
WORKDIR /hibp
ADD . /hibp
USER root
RUN pip install -r requirements.txt
CMD ["python","hibp_fn.py"]
