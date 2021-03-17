# Single page application 

The app is built with the Django framework based on course materials from zenva.com course "The Complete Responsive Web Design Course" (marked as obsolete in Jan 2021).

After this course, I cannot recommend this portal as a good place for learning. But the intellectual property, of course, is coded in this site. 

# Config 

sth about .env files 

and list of Environemnt variables with thier purpose in table 

## NGINX 

It is in proxy directory.... 

## Database 
Database MariaDB or MySQL can be hosted localy on docker.
Migration is provided to data base can be done with usage of predefined default values in settings.py and exectuion on localhost 
`python manage.py miakemigrations
python manage.py migrate`
Any additonal settings for connection may be provided in `.env` file. 

Second configuration file `docker-compose-deploy.yml` use NGINX as proxy server for testing in Debug mode on or off. 
This config use additional `MIGRATION` env variable that may be used to triger db migration on startup. 

Super User for django admin portal must be done via localhost manage.py file commands. 

# Development
## Local

### SonarQube 

sth about coverage 


## Docker


# Deployment 


## Docker
The remote docker compose contains no service for data base as on this level Data Base should be hosted on Robust and dedicated server. 
In case of deploying the app on multiple nodes media like static files are copied via rsync network of client-server relation.

Data base migration.
To Migrate data in production ENV the MIGRATION env variable may be used. 
Connection from local machine to remote data base may be better way to handle any error that may came along. 
For this purpose on root level of project modifiy .env file with connection for remote DB server and execute commands. 

## Database

## Rsync
