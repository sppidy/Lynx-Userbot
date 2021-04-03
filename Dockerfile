# LORD USERBOT
FROM liualvinas24/docker:groovy

#
# LORD
#
RUN git clone -b Lynx-Userbot https://github.com/KENZO-404/Lynx-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/KENZO-404/Lynx-Userbot/Lynx-Userbot/requirements.txt

CMD ["python3","-m","userbot"]
