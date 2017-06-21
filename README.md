# pachy_bug
This contains all the files to reproduce bug in incremental feature in pachyderm


# Commands to execute
```bash

# start pachyderm locally
minikube delete
minikube start
pachctl deploy local
pachctl port-forward &


# Put some data in repo numbers
pachctl create-repo numbers
pachctl put-file numbers master input.json -c -f input.json

```
