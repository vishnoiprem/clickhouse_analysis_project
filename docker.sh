docker-compose down
docker-compose up -d
docker-compose logs

docker exec -it clickhouse-server clickhouse-client --user admin --password admindocker-compose up -d
