# We're using Ubuntu 20.10
FROM kenzo404/docker:groovy

# Clone repo and prepare working directory

RUN git clone -b Lynx-Userbot https://github.com/KENZO-404/Lynx-Userbot.git /root/userbot
RUN pip install --upgrade pip setuptools
#working directory
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
