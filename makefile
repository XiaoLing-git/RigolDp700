CURRENT_DIR = $(CURDIR)

RM = rm -rf

RUN = poetry run

format:
	poetry run black $(CURRENT_DIR)/rigol_dp700

install:
	poetry install

shell:
	poetry shell


build: clean check
	poetry build

check:
	$(RUN) pre-commit run --all-files

clean:clean_chche
	$(RM) $(CURRENT_DIR)/dist

clean_chche:
	$(RM) $(CURRENT_DIR)/__pycache__
	$(RM) $(CURRENT_DIR)/.mypy_cache
	$(RM) $(CURRENT_DIR)/__pycache__/*
	$(RM) $(CURRENT_DIR)/.mypy_cache/*

	$(RM) $(CURRENT_DIR)/rigol_dp700/__pycache__
	$(RM) $(CURRENT_DIR)/rigol_dp700/.mypy_cache
	$(RM) $(CURRENT_DIR)/rigol_dp700/__pycache__/*
	$(RM) $(CURRENT_DIR)/rigol_dp700/.mypy_cache/*

commit:clean
	git add .
	git commit -m "$(msg)"

push:commit
	git push

debug:
	$(RUN) $(CURDIR)/main.py

echo:
	@echo $(CURRENT_DIR)
