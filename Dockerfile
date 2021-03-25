# We're using Ubuntu 20.10
FROM kenzo404/docker:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b Lynx-Userbot https://github.com/KENZO-404/Lynx-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN /bin/sh -c pip3 install -r https://raw.githubusercontent.com/KENZO-404/Lynx-Userbot/Lynx-Userbot/requirements.txt

CMD ["python3","-m","userbot"]
CMD ["bash"]
CMD ["/bin/bash"]
