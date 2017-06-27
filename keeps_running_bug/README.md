#first go to numbers folder 
cd ../numbers

#then execute all the commands in ../numbers/README.md

#change back to keeps_running_bug directory
cd ../keeps_running_bug

pachctl create-repo test_w
pachctl start-commit test_w master
pachctl finish-commit test_w <commit-id>

#Now commit everything in this folder into the `test_w` including the folder `configurations` and `pipelines`

#Now deploy all the pipelines inside the folder `/pipelines/*/*.json`

