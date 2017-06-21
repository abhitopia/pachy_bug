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
pachctl delete-all # press y
pachctl create-repo numbers
pachctl put-file numbers master input.json -c -f input.json

# Put the configuration file
pachctl create-repo poly
pachctl put-file poly  master configurations/x_multiply/x_multiply.json -c -f configurations/x_multiply/x_multiply.json

# deploy the pipeline
pachctl create-pipeline -f pipeline.json


# check the logs of the output 
pachctl get-logs --job <last-job-id>

# directories found by glob in script:
# ['/pfs/', '/pfs/numbers', '/pfs/numbers/input.json', '/pfs/config', '/pfs/config/configurations', '/pfs/config/configurations/x_multiply', '/pfs/config/configurations/x_multiply/x_multiply.json', '/pfs/out']

pachctl put-file poly  master configurations/x_multiply/x_multiply.json -c -f configurations/x_multiply/x_multiply.json


# modify the configuration file
# change configurations/x_multiply/x_multiply.json value from 3 to 10 and commit the configuration file again
pachctl put-file poly  master configurations/x_multiply/x_multiply.json -c -f configurations/x_multiply/x_multiply.json


# check the logs of the output 
pachctl get-logs --job <last-job-id>

# the job will fail the error being: IsADirectoryError: [Errno 21] Is a directory: '/pfs/config/configurations/x_multiply/x_multiply.json'
# looking at the glob of directories in the script we now see
#['/pfs/', '/pfs/numbers', '/pfs/numbers/input.json', '/pfs/config', '/pfs/config/configurations', '/pfs/config/configurations/x_multiply', '/pfs/config/configurations/x_multiply/x_multiply.json', '/pfs/config/configurations/x_multiply/x_multiply.json/configurations', '/pfs/config/configurations/x_multiply/x_multiply.json/configurations/x_multiply', '/pfs/config/configurations/x_multiply/x_multiply.json/configurations/x_multiply/x_multiply.json', '/pfs/out', '/pfs/out/output.json']

```
