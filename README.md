# pachy_bug
This contains all the files to reproduce bug in incremental feature in pachyderm


# Create number repo

`pachctl create-repo numbers`
`pachctl start-commit numbers master`
`pachctl finish-commit numbers <commit-id>`
