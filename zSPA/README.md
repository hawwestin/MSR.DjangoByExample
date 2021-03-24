# Single page application 

The app is built with the Django framework based on course materials from zenva.com course "The Complete Responsive Web Design Course" (marked as obsolete in Jan 2021). After this course, I cannot recommend this portal as a good place for learning. But the intellectual property, of course, is coded in this site. 

The general purpose of this file is to demonstrate the whole Web Development eco system needed to develop and test any product.

For demonstration this Django project has been kept as simple as possible but with usage of most common development tasks.  
 - File upload
 - DataBase migration 
 - Manage of static files from proxy
 
# Config 

List of Environemnt variables used to configure the app.

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
SECRET_KEY | *SECURITY WARNING:* keep the secret key used in production secret! | SECURITY WARNING: No Default Value
ALLOWED_HOSTS | Ip or/and DNS name of the server | *SECURITY WARNING:* No Default Value
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
Default port to listen is 8080.

## Database 

Database MariaDB or MySQL can be hosted locally on docker or remote server. \
Migration to database can be done with usage of predefined default values in `settings.py` or to server defined in `.env`. \
On localhost use \
`python manage.py miakemigrations`
And commit with \
`python manage.py migrate` 

On higher env level than localhost use `MIGRATE` environment variable with docker on startup.
With spread out environment this should be triggered only on demand. 
Default for execution data base migration is set to false.   

*SECURITY WARNING:* Super User for django admin portal must be done manually via localhost manage.py file commands configured to local or remote databese. 

## Docker

Configuration files provided in docker directory are mean to be used for development.
Docker files can be used to test application, deploy it on remote test environment and self 
host necessary tools that were used for development.

Default `docker-compose.yml` contains configuration in debug mode for web app development.
Second configuration file `docker-compose-deploy.yml` use NGINX as proxy server for testing in Debug mode on or off.
Third file `docker-compose-remote.yml` is provided to host the app on different environment than localhost. 
It can be called alfa, beta, integration or simple develop environment. 
Many companies name it accordingly for their development process.   

Some environment variables can be hold in dot env files. 

There isn't `docker-compose-prodcution.yml` as this app is for learning purpose and this part 
you can do on your own if you see value in this code to push it beyond.


# Development

It should be noticed that this repository is for learning purpose and the app is far from ready to go live production. This should demonstrate complex aspect of DevOps work needed to self host web application. 

## Localhost

Development on local machine support a few solutions which differentiate with DataBase server.
As Django require some database to run and host necessary data in case of insufficient resources, 
for local development may be used SQLite.

### Solution no.1 
On local you can use simple \
`python manage.py runserver`
And work with DEBUG set to True in `.env` file. \
DataBase may be hosted on Docker if you not have other resources for remote one. \
In this type of work you have full Django featured debugging app to work with. 
### Solution no.2
You can use `docker-compose.yml` file that binds to your local resources and listen on files changes. 
It is also bundled with MySQL server. The preferred way as this will encourage usage of docker.  

### Solution no.3
If you prefer to run python manage commands in your local terminal and 
do not have MySQL DB server you can start `docker-compose.yml` and stop the web app. 
DB will run without app. When you use all services you will have the same data inside. 

## SonarQube 

Static analysis tool that will keep guard on basic code style and catch issues. 
In enterprise environment such tools hosted on company networks help with team work and collaboration.
Once defined rule set will guide all developers with the same standards and principles.
For stand alone development it will provide some feedback even if you code alone.
As SonarQube provide good dashboard to display and browse code we can use it along PR to check 
if new code does not introduce any issues to code base. 

Beside analyzing code it also measure code coverage.
For purpose of analysing and making valid file for sonarqube project use most popular module [coveragepy](https://github.com/nedbat/coveragepy). 
Result of coverage script execution is a compressed xml file which is send to SonarQube Server. 
Default Quality Gate require 80% code coverage. 

To self host SonarQube service repository hold `docker-compose-sonarqube.yml` recipe.
Be advise that SQ server require 2gb of memory but 3gb is recommended. 
If its applicable SQ may be hosted on different device inside your network. 

File `sonarqube.sh` shell script can be executed before code is merged to Lead branch `master`.. 
To use the file a few settings must be provided as dotfiles. 
- `.sonarHostUrl` provide IP/DNS address to SonarQube service.
- `.sonarLogin` contains private access token generated on new project registration. For development purpose
community edition is sufficient. 

Each developer has different login token and may have different sonar address.  

When those tools are used from beginning many issues are neglect or barely noticeable.


# Deployment 


## Docker

The remote docker compose does not contains service for data base as on this level
 Data Base should be hosted on Robust and dedicated server. 
In case of deploying the app on multiple nodes media static files are copied via rsync network of client-server relation.

Data base migration.\
To Migrate data in remote ENV the MIGRATION env variable may be used. 
Connection from local machine to remote data base may be better way to handle any error 
that may came along. 
For this purpose on root level of project modify .env file with connection for remote DB 
server and execute commands. 

## Database

Should be used DataBase installed on dedicated machine that is secured to protect data. 
For this reason `docker-compose-remote.yml` does not contain db service. 
ENV file or inline environment variables should be provided instead. 

## Rsync

For media files backup there is client server [Rsync](https://linux.die.net/man/1/rsync) 
set with docker image of [eeacms/rsync](https://hub.docker.com/r/eeacms/rsync).
Basic usage you can find and learn [here](https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories).

### Client 
Client that is configured in `docker-compose-remote.yml` will use ssh keys aut generated on start up. 
The first handshake with server have to be done manually within container after you provide public key it the server. 
This have to be done once after you add new machine to development environment. 

Other solution is to mount volume to host keys like:
```yaml
   volumes:
      - static_data:/data
      - /etc/ssh/:/etc/ssh/
      - /root/.ssh/:/root/.ssh/
```
With this mounted keys form the host you inherit all known hosts and the handshake with new server will be valid inside docker container.

This can be achieved with simple dry run of Rsync command that provides address to your server. 
```bash
rsync -e 'ssh -p 2222 -i ~/.ssh/erysnc' -anvx --numeric-ids root@10.10.0.10:/data/ /docker/ersync/data
```

Cron task will periodically push and pull images form the server. Maintaining backup for data.
In this example app we were practicing sync of images but this solution will backup any data for given directories. 
In `docker-compose-remote.yml` you have to provide IP/DNS to your rsync Server. 

### Server
Server `docker-compose-rsync-server.com` contains pre configured server that can be deployed on remote. 
To connect client you have to add new environment key with name of `SSH_AUTH_KEY_{{nameOfTheClient}}` where
nameOfTheClient is for maintain purpose to easily identify keys in env variable list. 

If server keys are refreshed you can purge keys on client machines with command
```bash
ssh-keygen -f "/root/.ssh/known_hosts" -R "[10.10.0.10]:2222"
```
Then you have to perform handshake and download latest public key of the server. 
