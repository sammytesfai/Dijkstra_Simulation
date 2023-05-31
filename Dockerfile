FROM python:3.10
ENV SRC_DIR /usr/bin/src/webapp/src
COPY src/* ${SRC_DIR}/
COPY requirements.txt ${SRC_DIR}/requirements.txt
WORKDIR ${SRC_DIR}
ENV PYTHONUNBUFFERED=1
RUN pip3 install -r requirements.txt
EXPOSE 13800
CMD [ "python3", "router.py"]