
curl -X POST -H "Content-Type: application/json" -d '{
  "file": "/vagrant/Vagrantfile",
  "dir": "/home/kubos"
}' http://localhost:5000/flash

curl -X POST -H "Content-Type: application/json" -d '{
  "command": "cat Vagrantfile",
  "dir": "/home/kubos"
}' http://localhost:5000/run
