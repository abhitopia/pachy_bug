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

# Put the configuration file
pachctl create-repo poly
pachctl put-file poly  master configurations/x_multiply/x_multiply.json -c -f configurations/x_multiply/x_multiply.json

# deploy the pipeline
pachctl start-pipeline -f pipeline.json


# check the logs of the output 
pachctl get-logs --job <last-job-id>
## TODO (agis)

# modify the configuration file
# change pipeline.json value from 3 to 10 and commit the configuration file again
pachctl put-file numbers master configurations/x_multiply/x_multiply.json -c -f configurations/x_multiply.json

## Now you will notice failed job.
pachctl get-logs --job <last-job-id>
## TODO(agis)




```
