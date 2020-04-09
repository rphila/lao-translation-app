FROM ubuntu:18.04
#FROM python:3.6
# -alpine

RUN apt-get update \
    && apt-get install tesseract-ocr -y \
    && apt-get install python3 -y \
    && apt-get install python3-pip -y

# Set an environment variable with the directory
# where we'll be running the app
ENV APP /app

# Create the directory and instruct Docker to operate
# from there from now on
RUN mkdir $APP
WORKDIR $APP

# Expose the port uWSGI will listen on
EXPOSE 5000

# Copy the requirements file in order to install
# Python dependencies
COPY requirements.txt .
# Install Python dependencies
RUN pip3 install -r requirements.txt

# We copy the rest of the codebase into the image
COPY . .

COPY lao.traineddata  /usr/share/tesseract-ocr/4.00/tessdata/lao.traineddata
COPY GoogleTranslateProject-4778da0a83ca.json  /app
ENV GOOGLE_APPLICATION_CREDENTIALS /app/GoogleTranslateProject-4778da0a83ca.json

#ADD . /app
WORKDIR /app

CMD ["python3", "app.py"]
