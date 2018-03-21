include config.env

VERSION ?= latest
REPO = twix2ismrmrd
NAME = twixconverter
INSTANCE = default

.PHONY: build push shell run start stop rm release

build:
	docker build -t $(REPO):$(VERSION) .

push:
	docker push $(REPO):$(VERSION)

shell:
	docker run --rm --name $(NAME)-$(INSTANCE) -i -t $(VOLUMES) $(REPO):$(VERSION) /bin/bash

run:
	docker run --rm --name $(NAME)-$(INSTANCE) $(VOLUMES) $(REPO):$(VERSION)

start:
	docker run -d --name $(NAME)-$(INSTANCE) $(VOLUMES) $(REPO):$(VERSION)

stop:
	docker stop $(NAME)-$(INSTANCE)

rm:
	docker rm $(NAME)-$(INSTANCE)

release: build
	make push -e VERSION=$(VERSION)

default: build