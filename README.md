# k8s-gcp-geo-distribution

[<small>khaledalam/k8s-gcp-geo-distribution</small>](https://hub.docker.com/repository/docker/khaledalam/k8s-gcp-geo-distribution/)<br />
[![Docker Pulls](https://img.shields.io/docker/pulls/khaledalam/k8s-gcp-geo-distribution.svg)](https://hub.docker.com/r/khaledalam/k8s-gcp-geo-distribution/)
[![Docker Version](https://img.shields.io/docker/v/khaledalam/k8s-gcp-geo-distribution?sort=semver)](https://hub.docker.com/r/khaledalam/k8s-gcp-geo-distribution/)


APP has 2 different versions (determined by env var `APP_COUNTRY`) Override by K8s(`spec.containers.env`):
- US 
- UAE

Each version placed on a K8s deployment<->service.

### Diagram:
<img src="infra-diagram.png" />

K8s resources:
```
NAME                                  READY   STATUS    RESTARTS   AGE
pod/deployment-uae-5b7d4b6dd7-7mlsp   1/1     Running   0          49s
pod/deployment-uae-5b7d4b6dd7-kvtmc   1/1     Running   0          49s
pod/deployment-us-6db549b746-bhzxt    1/1     Running   0          49s
pod/deployment-us-6db549b746-rp9kw    1/1     Running   0          49s

NAME                  TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
service/kubernetes    ClusterIP      10.96.0.1      <none>        443/TCP        7d2h
service/service-uae   LoadBalancer   10.106.99.18   <pending>     80:30947/TCP   49s
service/service-us    LoadBalancer   10.99.99.39    <pending>     80:31567/TCP   49s

NAME                             READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/deployment-uae   2/2     2            2           49s
deployment.apps/deployment-us    2/2     2            2           49s

NAME                                        DESIRED   CURRENT   READY   AGE
replicaset.apps/deployment-uae-5b7d4b6dd7   2         2         2       49s
replicaset.apps/deployment-us-6db549b746    2         2         2       49s
```



Routing:
- 1st method: `(costly solution)`
    - Used GCP function and node package [geoip-lite](https://github.com/geoip-lite/node-geoip)(based on maxmind) for locating the user ip country and routing the traffic to k8s ingress paths `/us` or `/uae`.
      - GCP function 2nd-gen has more `Runtime, build, connections and security settings` such as Concurrency(Maximum concurrent requests per instance).
  - Improvements:
    - Replace GCP function with lower price solution
    - Caching maxmind api calls
    - ...
- Other methods: `investigating ingress-nginx custom annotation and other solutions`