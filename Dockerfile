FROM osgeo/gdal:ubuntu-small-latest

WORKDIR /user/src/app

RUN apt-get update
RUN apt-get install traceroute
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y iputils-ping
RUN python3 -m pip install --upgrade pip
COPY ./requirements.txt /user/src/app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 80
COPY . . 

CMD ["flask","run","--host","0.0.0.0","--port", "80"]
