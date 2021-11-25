#!/bin/bash
set -x

if [[ $# -lt 4 ]] ; then
    echo "Please supply params: DOCKER_REPOSITORY TAG_MINOR TAG_PATCH MARKETPLACE_TOOLS_TAG"
    echo "e.g. gcr.io/electrifai-public/models 1.0 1.0.2 0.10.6"
    exit 1
fi

DOCKER_REPOSITORY=$1
TAG_MINOR=$2
TAG_PATCH=$3
MARKETPLACE_TOOLS_TAG=$4

# app image
docker build --no-cache -t ${DOCKER_REPOSITORY}:${TAG_MINOR} appimage
docker tag ${DOCKER_REPOSITORY}:${TAG_MINOR} ${DOCKER_REPOSITORY}:${TAG_PATCH} 
docker push ${DOCKER_REPOSITORY}:${TAG_MINOR}
docker push ${DOCKER_REPOSITORY}:${TAG_PATCH} 

# deployer image
docker build --no-cache -t ${DOCKER_REPOSITORY}/deployer:${TAG_MINOR} -f deployer/Dockerfile --build-arg MARKETPLACE_TOOLS_TAG=${MARKETPLACE_TOOLS_TAG} --build-arg REGISTRY=${DOCKER_REPOSITORY} --build-arg TAG=${TAG_PATCH}  .
docker tag ${DOCKER_REPOSITORY}/deployer:${TAG_MINOR} ${DOCKER_REPOSITORY}/deployer:${TAG_PATCH} 
docker push ${DOCKER_REPOSITORY}/deployer:${TAG_MINOR}
docker push ${DOCKER_REPOSITORY}/deployer:${TAG_PATCH} 

# prometheus dependency
docker tag gcr.io/google-containers/prometheus-to-sd:v0.9.2 ${DOCKER_REPOSITORY}/prometheus-to-sd:${TAG_MINOR}
docker tag ${DOCKER_REPOSITORY}/prometheus-to-sd:${TAG_MINOR} ${DOCKER_REPOSITORY}/prometheus-to-sd:${TAG_PATCH} 
docker push ${DOCKER_REPOSITORY}/prometheus-to-sd:${TAG_MINOR}
docker push ${DOCKER_REPOSITORY}/prometheus-to-sd:${TAG_PATCH} 

# debian9 dependency
docker tag marketplace.gcr.io/google/debian9:latest ${DOCKER_REPOSITORY}/debian9:${TAG_MINOR}
docker tag ${DOCKER_REPOSITORY}/debian9:${TAG_MINOR} ${DOCKER_REPOSITORY}/debian9:${TAG_PATCH} 
docker push ${DOCKER_REPOSITORY}/debian9:${TAG_MINOR}
docker push ${DOCKER_REPOSITORY}/debian9:${TAG_PATCH} 

# tester image
docker build --no-cache -t ${DOCKER_REPOSITORY}/tester:${TAG_MINOR} -f apptest/tester/Dockerfile apptest/tester
docker tag ${DOCKER_REPOSITORY}/tester:${TAG_MINOR} ${DOCKER_REPOSITORY}/tester:${TAG_PATCH} 
docker push ${DOCKER_REPOSITORY}/tester:${TAG_MINOR}
docker push ${DOCKER_REPOSITORY}/tester:${TAG_PATCH} 