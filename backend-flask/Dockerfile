FROM python:3.10-slim-buster

# Inside Container
#   make a new folder inside container
WORKDIR /backend-flask

# Outside Container --> Inside Container
#   this containers the libraries we want to install to run the app
COPY requirements.txt requirements.txt

# Inside Container
#   install the python libraries used for the app
RUN pip3 install -r requirements.txt

# Outside Container --> Inside Container
#   . means everything in the current directory
#   first period . - '/backend-flask' outside the container
#   second period . - '/backend-flask' inside the container
COPY . .

# Set Environment Variables (Env Vars)
#   set inside the container and remains set when the container is running
ENV FLASK_ENV=development

EXPOSE ${PORT}

# CMD (Command)
# python3 -m flask run --host=0.0.0.0 --port=4567
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]