## How to run this web application

1. Download the latest version of Python, either directly or through the Anaconda distribution.

2. Download Docker for Desktop [here](https://www.docker.com/products/docker-desktop). Installation guides for various OS's can be found [here](https://docs.docker.com/desktop/)

3. Ensure Docker is running in the background.

4. Move to the 'project' directory and run the following command in CMD to build the container:

> * docker build -t predict-app .

5. Once the container is built, it can be run on port 5000 of the container, and with port 5000 of the host OS listening also on port 5000, using the following command:

> * docker run -d -p 5000:5000 predict-app

6. Then to access the containerized application, go to http://127.0.0.1:5000/ in a web browser.

7. To stop the container running, first list the containers currently running with the following command:

> * docker container ls

8. Identify the CONTAINER ID of the container you wish to stop running, then enter the following command, replacing CONTAINER ID as appropriate:

> * docker kill CONTAINER ID

9. Finally run the following command to destroy the container:

> * docker rm CONTAINER ID
