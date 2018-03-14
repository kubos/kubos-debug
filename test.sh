#
# curl -X POST -H "Content-Type: application/json" -d '{
#   "file": "/vagrant/hexes",
#   "dir": "/home/kubos"
# }' http://localhost:8000/flash


curl -X POST -H "Content-Type: application/json" -d '{
  "command": "ps",
  "dir": "/home/kubos"
}' http://localhost:8000/run
