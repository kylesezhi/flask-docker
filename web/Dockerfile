FROM kkarczmarczyk/node-yarn:7.6
MAINTAINER Kyle Bedell "kyle.bedell@gmail.com
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app/static
RUN yarn install
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
