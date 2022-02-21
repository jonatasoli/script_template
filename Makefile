POETRY = @poetry
POETRY_REQUIREMENTS = export -f requirements.txt --output requirements.txt

## @ Poetry activate env
.PHONY: activate
activate:
	${POETRY} shell

## @ Install Dependencies
.PHONY: install
install:
	${POETRY} install

## @ Generate requirements
.PHONY: requirements
requirements:
	rm requirements.txt
	${POETRY} ${POETRY_REQUIREMENTS}

## @ Run Tests
.PHONY: test
test:
	pytest -s

## @ Format code
.PHONY: format
format:
	@blue .
	@isort .

## @ lint check
.PHONY: lint
lint:
	@blue --check
	@isort --check
	@prospector

## @ security check
.PHONY: sec
sec:
	@safety

.PHONY: help
help:
	@python help.py
