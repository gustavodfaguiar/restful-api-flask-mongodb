PORT=5000
DOCKER_CMD=docker exec -it restful-api-flask-mongodb_web_1

help: ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

setup: ## Setup
	docker-compose build

welcome:
	@echo "Welcome http://localhost:$(PORT)"

start: welcome ## Start
	docker-compose up

shell:
	${DOCKER_CMD}

stop: ## Stop
	docker-compose down

test: ## Test
	${DOCKER_CMD} pytest
