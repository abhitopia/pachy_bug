```bash
## assumes all below commands are run from pachy_bug/keeps_running_bug/

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

pachctl list-job
ID                                   OUTPUT COMMIT                                              STARTED       DURATION           RESTART PROGRESS STATE
1d58ac12-814d-4e3c-a837-440ff7e45813 _test_w_b_times_x/a4a574c59870438db49e627affecafe1         3 minutes ago Less than a second 0       1 / 1    success
26a56b67-7bba-4f42-be32-3a942ae36ab6 _test_w_b_times_x/98bb5dd7fa144e69bdb76babf4b744a3         3 minutes ago Less than a second 0       0 / 0    success
15c875db-5ec5-4d0c-b74e-11eecf70c7df _test_w_a_times_x_squared/-                                3 minutes ago -                  0       0 / 1    running
09cbc3ab-7e16-463a-bc16-674ac2d4e231 _test_w_a_times_x_squared/22a1b2d83a684ac2a99ee059d8549a3e 3 minutes ago Less than a second 0       0 / 0    success
0b0ec066-1655-4183-ac86-c8bbf33c7eab _test_w_x_squared/c822d3a888a04410a02441a276e3593d         3 minutes ago 1 seconds          0       1 / 1    success
000ead86-4164-41a0-8d91-dd26a5441b0e _test_w_x_squared/88991af6559c455d81e1ebacab78492c         3 minutes ago Less than a second 0       0 / 0    success
8671d5b4-da08-4516-b92e-7cc6b1165768 _test_w_x_squared/f6702dac40e84a3c8c523044046a8862         3 minutes ago Less than a second 0       0 / 0    success
```

