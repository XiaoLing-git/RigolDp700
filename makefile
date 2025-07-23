CURRENT_DIR = $(CURDIR)

format:
	poetry run black $(CURRENT_DIR)/rigol_dp700

install:
	poetry install

shell:
	poetry shell


build: clean
	poetry build

check:format
	poetry run mypy  $(CURRENT_DIR)/rigol_dp700

clean:clean_chche
	rm -rf $(CURRENT_DIR)/dist

clean_chche:
	rm -rf $(CURRENT_DIR)/__pycache__
	rm -rf $(CURRENT_DIR)/.mypy_cache
	rm -rf $(CURRENT_DIR)/__pycache__/*
	rm -rf $(CURRENT_DIR)/.mypy_cache/*

	rm -rf $(CURRENT_DIR)/rigol_dp700/__pycache__
	rm -rf $(CURRENT_DIR)/rigol_dp700/.mypy_cache
	rm -rf $(CURRENT_DIR)/rigol_dp700/__pycache__/*
	rm -rf $(CURRENT_DIR)/rigol_dp700/.mypy_cache/*

commit:clean check
	git add .
	git commit -m "$(msg)"

push:commit
	git push

debug:
	python $(CURDIR)/main.py

echo:
	@ech o $(CURRENT_DIR)