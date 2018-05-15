# oracle-weblogic
DockerFile for weblogic


Docker push images:

1. docker login --username=admin --password=HaCZtDlrDxOWEDiYiB4eelUi2g_IvmeQcVLq0ROCvUk docker-registry.default.svc:5000
2. docker tag b6fedd38446c docker-registry.default.svc:5000/openshift/oracle-jre8:latest
3. docker push  docker-registry.default.svc:5000/openshift/oracle-jre8:latest
