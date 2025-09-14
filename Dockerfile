# syntax=docker/dockerfile:1
# build with: docker build . -t binexp_workshop:latest
# launch with: docker run -it binexp_workshop:latest
FROM python:3.13-bookworm

ENV DEBIAN_FRONTEND=noninteractive PIP_NO_CACHE_DIR=1

RUN apt update && apt install -y --no-install-recommends tmux neovim nano less curl p7zip-full build-essential sudo gcc g++ make cmake gdb gdbserver ltrace strace binutils python3 python3-pip nasm checksec && rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash student
RUN echo "student ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

WORKDIR /tmp
#get rp++
RUN curl -fsSL "https://github.com/0vercl0k/rp/releases/download/v2.1.4/rp-lin-gcc.zip" -o /tmp/rp-lin-gcc.zip && 7z x /tmp/rp-lin-gcc.zip -y && mv /tmp/rp-lin /home/student/ && chown student:student /home/student/rp-lin && rm -rf /tmp/*

RUN pip3 install pwntools keystone-engine

WORKDIR /home/student/
COPY labs/ /home/student/labs/
COPY .gdbinit /home/student/.gdbinit
RUN chown student:student /home/student -R
USER student
CMD ["setarch", "x86_64", "-R", "tmux"]
