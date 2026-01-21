# Commands Used

docker pull nginx
docker run --name nginx-test -d -p 8080:80 nginx

docker ps
curl localhost:8080

# Cleanup 
docker stop nginx-test
docker rm nginx-test 
