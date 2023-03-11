SHELL := /bin/bash
include config.env

DOCKER_RUN_BASE := docker run -it --rm
DOCKER_RUN_BASE += --volume $(shell pwd):/opt/app
DOCKER_RUN_BASE += --user $(shell id -u):$(shell id -g)
DOCKER_RUN_BASE += --net=host $(APP_NAME)-dev:latest

.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

docker-grant: ## Grant permission on docker.sock
	sudo setfacl -m user:$(USER):rw /var/run/docker.sock

docker-build-dev: ## Build the Docker development image
	docker build -t $(APP_NAME)-dev -f Dockerfile.dev .

docker-shell: ## Launch Docker shell
	$(DOCKER_RUN_BASE)

docker-pytest-watch: ## Run test on change
	$(DOCKER_RUN_BASE) /opt/venv/bin/pytest-watch

docker-test: ## Run test on change
	$(DOCKER_RUN_BASE) /bin/bash -c "mypy tenisgo/ && pytest"

docker-start: ## Start django
	$(DOCKER_RUN_BASE) bash -c "cd $(APP_NAME) && ./manage.py migrate && ./manage.py runserver"
