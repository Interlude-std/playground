# base image
FROM python:3.8.5

ARG project_dir=/work

# workdir にファイル等追加
#ADD yunbot.py $project_dir
#ADD yuntaku_bot.py $project_dir
#ADD credential.py $project_dir
#ADD yuna8313_threewords.pickle $project_dir
ADD requirements.txt $project_dir/

ADD yunbot_cron /etc/cron.d/yunbot_cron
RUN chmod 0644 /etc/cron.d/yunbot_cron

# workdir
# なければ新規作成
WORKDIR $project_dir/

# cronインストール
RUN apt-get update
RUN apt-get install -y cron

# VIインストール
RUN apt-get update
RUN apt-get install -y vim

# upgrade pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# cron起動
RUN crontab /etc/cron.d/yunbot_cron
#CMD cron
