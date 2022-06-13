FROM ubuntu:22.04
RUN apt update && apt -y upgrade
RUN apt -y install git python3 python3-pip
RUN pip3 install uvicorn
RUN pip3 install fastapi
RUN mkdir /root/project
WORKDIR /root/project
RUN git clone https://github.com/anushapv2000/restapi-service.git
WORKDIR /root/project/restapi-service

CMD ["uvicorn","restapi:app","--host","0.0.0.0","--port","8080"]

