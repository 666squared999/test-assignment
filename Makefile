.PHONY: build
build:
	sudo cp nginx.conf /etc/nginx/nginx.conf
	sudo /etc/init.d/nginx restart
	sudo docker-compose up -d --build

.DEFAULT_GOAL := build