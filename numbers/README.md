pachctl create-repo numbers
pachctl start-commit numbers master
pachctl finish-commit numbers <commit-id>


pachctl put-file -c input.json -f input.json  # to commit the input.json