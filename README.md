# k8s-gcp-geo-distribution

[<small>khaledalam/k8s-gcp-geo-distribution</small>](https://hub.docker.com/repository/docker/khaledalam/k8s-gcp-geo-distribution/)<br />
[![Docker Pulls](https://img.shields.io/docker/pulls/khaledalam/k8s-gcp-geo-distribution.svg)](https://hub.docker.com/r/khaledalam/k8s-gcp-geo-distribution/)
[![Docker Version](https://img.shields.io/docker/v/khaledalam/k8s-gcp-geo-distribution?sort=semver)](https://hub.docker.com/r/khaledalam/k8s-gcp-geo-distribution/)


Core APP has 2 different versions (determined by env var `APP_COUNTRY`) Override by K8s(`spec.containers.env`):
- US 
- UAE


Each version placed on a K8s deployment<->service.


Routing:
- 1st method: `-`
- 2nd method: `-`