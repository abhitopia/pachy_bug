```bash
# start afresh
minikube delete
minikube start
pachctl deploy local
pachctl port-forward &

# Create numbers repo like following
cd ../numbers
pachctl create-repo numbers
pachctl start-commit numbers master
pachctl finish-commit numbers <commit-id>
pachctl put-file numbers master -c input.json -f input.json

# sanity check
pachctl list-commit numbers

# Create test_w repo like following
cd ../keeps_running_bug
pachctl create-repo test_w
pachctl start-commit test_w master
pachctl finish-commit test_w <commit-id>
pachctl put-file -r test_w master -c -f .

#Now deploy all the pipelines inside the folder `/pipelines/*/*.json`
pachctl create-pipeline -f pipelines/x_squared/x_squared.json
pachctl create-pipeline -f pipelines/a_times_x_squared/a_times_x_squared.json
pachctl create-pipeline -f pipelines/b_times_x/b_times_x.json
pachctl create-pipeline -f pipelines/a_times_x_squared_plus_b_times_x/a_times_x_squared_plus_b_times_x.json
pachctl create-pipeline -f pipelines/a_times_x_squared_plus_b_times_x_plus_c/a_times_x_squared_plus_b_times_x_plus_c.json
```
