up:
	docker compose up

upd:
	docker compose up -d

down:
	docker compose down

build:
	docker compose build

restart:
	make down && make up