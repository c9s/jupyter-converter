
all:
	docker build \
		--tag yoanlin/jupyter-converter:latest \
		--tag asia.gcr.io/linker-aurora/jupyter-converter:latest \
		.
