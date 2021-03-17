# Single page application 

The app is built with the Django framework based on course materials from zenva.com course "The Complete Responsive Web Design Course" (marked as obsolete in Jan 2021). After this course, I cannot recommend this portal as a good place for learning. But the intellectual property, of course, is coded in this site. 

The general purpose of this file is to demonstrate the whole Web Development eco system needed to develop and test any product.

# Config 

List of Environemnt variables used to configure the app.\

Some may be provided in `.env` files loaded in section `env_file`  inside docker-compose-\*.yml file.  
ENV file is a list of environemnt variables that you don't want to repeat and store it once. Structure of the files looks liek this
```.env
SECRET_KEY = 'ChangeME!'
ALLOWED_HOSTS = '127.0.0.1, localhost`
DEBUG = False
DB_NAME = 'zspa'
DB_USER = 'user'
DB_PASS = 'password'
DB_HOST = '10.10.0.10'
DB_PORT = '3306'
googleForm = 'https://docs.google.com/forms/d/e/1FAI....
googleMaps = 'https://www.google.com/maps/embed?pb=!1m18...
```

Variable | Description | Deafult 
------------ | ------------- | -------------
DEBUG | SECURITY WARNING: don't run with debug turned on in production! | False
SECRET_KEY |  SECURITY WARNING: keep the secret key used in production secret! | SECURITY WARNING: No Default Value
ALLOWED_HOSTS | Ip or/and DNS name of the server | SECURITY WARNING: No Default Value
DB_NAME | Name of databese in database server | zspa
DB_USER | Name of user that have access to database | user
DB_PASS | Password for the database user | password
DB_HOST | IP or/and DNS name of the database server | localhost
DB_PORT | Port to connect to the database | 3306
MIGRATE | Execute migration on startup. Default docker command applied in `scripts\entrypoint.sh` | false
googleForm | Link to google form for contact purpose | Empty
googleMaps | Link to google maps of your company place | Empty 

## NGINX 

Used as proxy to serve website and static files from the same host. 
Aplied configuration allow to upload images up to 5M. Can be changed in proxy\default.conf `client_max_body_size` variable. \
Default port to listen is 8080.\

## Database 

Database MariaDB or MySQL can be hosted localy on docker or remote server. \
Migration to database can be done with usage of predefined default values in `settings.py` or to server defined in `.env`. \
On localhost use \
`python manage.py miakemigrations`
And commit with \
`python manage.py migrate`\

On higher env level than localhost use `MIGRATE` environment variable with docker on startup.

SECURITY WARNING: Super User for django admin portal must be done manually via localhost manage.py file commands configured to local or remote databese. 

# Development
## Local

### SonarQube 

sth about coverage 


## Docker

Second configuration file `docker-compose-deploy.yml` use NGINX as proxy server for testing in Debug mode on or off. 

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
