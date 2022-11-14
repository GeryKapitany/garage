docker run -d \
--name=mariadb \
-e PUID=1000 \
-e PGID=1000 \
-e TZ=Europe/Budapest \
-p 3306:3306 \
-v /data/docker/mariadb/config:/config \
--restart unless-stopped \
lscr.io/linuxserver/mariadb
