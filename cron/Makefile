#include ../jupyterhub/.env

user ?= calvinpy
DOCKER_CRON_IMAGE ?= labs/cron
DOCKER_CRON_BOX ?= labs.cron
COMPOSE_SERVICE ?= cron

build:
	@docker build -t $(DOCKER_CRON_IMAGE) .

rmi:
	@cd ..; $(MAKE) -s rmi image=$(DOCKER_CRON_IMAGE)

commit:
	@docker commit $(DOCKER_CRON_BOX) $(DOCKER_CRON_IMAGE)

start:
	@docker-compose -f ../docker-compose.yml up -d $(COMPOSE_SERVICE)

ci:	build start

.PHONY: build rmi commit start ci
