CURRENT_DIR = $(CURDIR)

format:
	poetry run black $(CURRENT_DIR)/src

install:
	poetry install

shell:
	poetry shell

depend:shell
	poetry run pip install -r .\requirements.txt

build: clean
	poetry build

check:
	poetry run mypy  $(CURRENT_DIR)/src

clean:
	rm -rf dist

commit:clean format check
	git add .
	git commit -e $(msg)

echo:
	@echo $(CURRENT_DIR)