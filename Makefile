.PHONY: clean clean-dist test

VENV=.venv
VENV_ACTIVATE=. $(VENV)/bin/activate
BUMPTYPE=patch

$(VENV):
	virtualenv $(VENV)
	$(VENV_ACTIVATE); pip install tox bumpversion twine

test: $(VENV)
	$(VENV_ACTIVATE); tox

dist: clean-dist
	python setup.py sdist
	ls -ls dist

release: dist
	$(VENV_ACTIVATE); twine upload dist/*

bump: $(VENV)
	$(VENV_ACTIVATE); bumpversion $(BUMPTYPE)
	git show -q
	@echo
	@echo "SUCCESS: Version was bumped and committed. Now push the commit:"
	@echo
	@echo " 	git push origin master && git push --tags"

clean-dist:
	rm -rf dist

clean: clean-dist
	rm -rf $(VENV)

