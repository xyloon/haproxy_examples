FROM ubuntu:22.04

ARG IGID
ARG IUID
ENV IGID 1100
ENV IUID 1100

RUN apt update && apt install -y ttyd tmux ssh sudo && apt clean
RUN addgroup bai --gid $IGID && \
    adduser --disabled-password --uid $IUID --gid $IGID --gecos "" bai && \
    echo 'bai:bai' | chpasswd && \
    usermod -aG sudo bai && \
    echo 'work ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
WORKDIR /home/bai
Expose 7681/tcp
CMD su bai -c "/usr/bin/ttyd -p 7681 -b /bai/maintenance -c id:password /usr/bin/tmux"