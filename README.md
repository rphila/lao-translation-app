# lao-translation-app
- This web app performs OCR from an uploaded image containing Laotion language script and returns it as English text.
- Sample images to upload are in `sample-images` folder

#### Prerequisite
* docker: https://docs.docker.com/get-docker/ 

#### Local Deployment
To run locally:
```docker-compose up --build```

#### Dockerhub Deployment
https://hub.docker.com/repository/docker/rphila/lao-translation-app

To push updated image onto dockerhub:

```
docker build ./web -t rphila/lao-translation-app:latest

docker push rphila/lao-translation-app:latest
```

To deploy image from dockerhub:

```
docker pull rphila/lao-translation-app:latest

docker run -p 5000:5000 --rm rphila/lao-translation-app:latest
```

* Note: docker needs to be installed onto the server first 

Example using Amazon Linux AMI EC2 instance:
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html#install_docker

```
sudo yum update -y
sudo yum install docker
sudo service docker start

docker login
<enter dockerhub credentials>

docker pull rphila/lao-translation-app:latest
docker run -p 5000:5000 --rm rphila/lao-translation-app:latest
```

