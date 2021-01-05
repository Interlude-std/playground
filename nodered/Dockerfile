# base image
FROM node

ARG project_dir=/work

# workdir
# なければ新規作成
WORKDIR $project_dir/


RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y sudo


RUN apt-get update
#RUN apt-get install -y npm

# upgrade pip
RUN sudo apt-get install -y python3-pip

RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

RUN sudo npm install -g --unsafe-perm node-red