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

check:format
	poetry run mypy  $(CURRENT_DIR)/src

clean:clean_pychche
	rm -rf $(CURRENT_DIR)/dist

clean_pychche:
	rm -rf $(CURRENT_DIR)/__pycache__
	rm -rf $(CURRENT_DIR)/.mypy_cache
	rm -rf $(CURRENT_DIR)/__pycache__/*
	rm -rf $(CURRENT_DIR)/.mypy_cache/*

commit:clean format check
	git add .
	git commit -m "$(msg)"

push:commit
	git push

debug:
	python $(CURDIR)/main.py

echo:
	@echo $(CURRENT_DIR)