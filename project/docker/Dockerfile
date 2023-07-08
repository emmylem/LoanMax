FROM python:3.6
LABEL maintainer "emmylem"
RUN apt-get update
RUN mkdir /loanmax
WORKDIR /loanmax
COPY . /loanmax
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["sh","project/docker/docker_script.sh"]
EXPOSE 5000
EXPOSE 5432
RUN chmod +x project/docker/docker_script.sh
CMD ["/bin/bash", "project/docker/docker_script.sh"]
