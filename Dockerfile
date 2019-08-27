FROM python:3.7-slim-buster  

# Install required packages
RUN apt-get update && apt-get -y install -y \
    texlive-latex-base \
    texlive-fonts-recommended
RUN DEBIAN_FRONTEND=noninteractive pip3 install pyx pynomo numpy scipy

# Add our python app code to the image
RUN mkdir -p /app
ADD . /app
WORKDIR /app
