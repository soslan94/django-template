# jenkins/Dockerfile
FROM jenkins/jenkins:lts-jdk11

# временно root для установки docker client
USER root

# минимальная установка docker client (используем пакет из дистрибутива для простоты)
RUN apt-get update \
 && apt-get install -y --no-install-recommends docker.io \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# возвращаемся к jenkins-пользователю
USER jenkins

EXPOSE 8080 50000