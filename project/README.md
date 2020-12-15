Move to the 'project' directory and run the following command in CMD to build the container:

* docker build -t predict-app .

Once the container is built, it can be run on port 5000 of the container, and with port 5000 of the host OS listening also on port 5000, using the following command:

* docker run -d -p 5000:5000 predict-app

Then to access the containerized application, go to http://1.0.0.127:5000 in a web browser.

To stop the container running, first list the containers currently running with the following command:

* docker container ls

Identify the CONTAINER ID of the container you wish to stop running, then enter the following command, replacing CONTAINER ID as appropriate:

* docker kill CONTAINER ID 

Finally run the following command to destroy the container:

* rm CONTAINER ID