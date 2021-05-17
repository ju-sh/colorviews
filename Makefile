first-upload: dist/
	python3 -m twine upload dist/*

update-upload: dist/
	python3 -m twine upload --skip-existing dist/* 

.PHONY: build purge_cache clean cov test mypy pylint flake8 check-manifest bumpversion

build:
	rm -rf build/ dist/ src/colorviews.egg-info/
	python3 setup.py sdist bdist_wheel

purge-cache:
	rm -r .coverage .mypy_cache/ .pytest_cache/

clean:
	rm -r .coverage .mypy_cache/ .pytest_cache/ .tox/

cov:
	coverage run -m pytest tests/ && coverage html

test:
	pytest tests/

mypy:
	mypy src/

pylint:
	pylint src/colorviews/

flake8:
	flake8 src/colorviews/ tests/

check-manifest:
	check-manifest .

vulture:
	vulture . whitelist.py

change-version:
	# Assumption: Current version = 0.1-alpha0
	sed -i 's/version="0.1-alpha0"/version="0.1-alpha0"/' setup.py
	sed -i 's/__version__ = "0.1-alpha0"/__version__ = "0.1-alpha0"/' src/colorviews/__init__.py
