.PHONY: clean clean-dist test

VENV=.venv
VENV_ACTIVATE=. $(VENV)/bin/activate
BUMPTYPE=patch

$(VENV):
	virtualenv $(VENV)
	$(VENV_ACTIVATE); pip install tox bumpversion twine 'readme_renderer[md]'

test: $(VENV)
	$(VENV_ACTIVATE); tox

dist: clean-dist
	$(VENV_ACTIVATE); python setup.py sdist bdist_wheel
	ls -ls dist
	tar tzf dist/*.tar.gz
	$(VENV_ACTIVATE); twine check dist/*

test-release: clean test dist
	$(VENV_ACTIVATE); twine upload --repository-url https://test.pypi.org/legacy/ dist/*

release: clean test dist
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

