
all:
	docker build \
		--tag yoanlin/jupyter-converter:latest \
		--tag asia.gcr.io/linker-aurora/jupyter-converter:latest \
		.

push-gcr:
	gcloud docker -- push asia.gcr.io/linker-aurora/jupyter-converter

push-docker:
	docker push yoanlin/jupyter-converter

push: push-gcr push-docker
