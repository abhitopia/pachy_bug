echo "Running pachctl delete-all"
echo y | pachctl delete-all
echo "Creating repo1 repo2 repo3"
pachctl create-repo repo1
pachctl create-repo repo2
pachctl create-repo repo3
echo "file1 output" > file1
echo "file2 output" > file2
echo "file3 output" > file3
echo "Commiting file1 to repo1 on master"
echo "Commiting file2 to repo2 on master"
echo "Commiting file3 to repo3 on _test"
pachctl put-file repo1 master -c -f file1
pachctl put-file repo2 master -c -f file2
pachctl put-file repo3 _test -c -f file3
echo "Creating the pipeline"
pachctl create-pipeline -f pipeline.json

