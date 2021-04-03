# We're using Ubuntu 20.10
FROM kenzo404/docker:lynx-userbot

#
# Clone repo and prepare working directory
#
RUN git clone -b Lynx-Userbot https://github.com/KENZO-404/Lynx-Userbot /root/LynxUserbot
RUN mkdir /root/LynxUserbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/LynxUserbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/KENZO-404/Lynx-Userbot/Lynx-Userbot/requirements.txt

CMD ["python3","-m","userbot"]
