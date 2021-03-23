#!/usr/bin/env bash
git describe --contains --all HEAD > .branch_name
BRANCH=`cat .branch_name`
sonarHostUrl=`cat .sonarHostUrl`
sonarLogin=`cat .sonarLogin`

echo $BRANCH
source venv/scripts/activate
coverage erase
coverage run --source='zSPA' zSPA/manage.py test spa
coverage xml
deactivate

sonar-scanner.bat \
-D"sonar.projectKey=zSpa-dev" \
-D"sonar.host.url=$sonarHostUrl" \
-D"sonar.login=$sonarLogin" \
-D"sonar.projectVersion=$BRANCH" \
-D"sonar.python.coverage.reportPaths=coverage.xml"
