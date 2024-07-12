run:
	python -m echoer
docker_build:
	docker build . -t echoer
docker_run:
	docker run --rm -p 5555:5555 echoer
test:
	curl http://localhost:5555 -d '{"say": "hello"}' -H 'Content-Type: application/json'
