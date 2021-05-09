update_upload: dist/
	python3 -m twine upload --skip-existing dist/* 

.PHONY: build purge_cache clean cov test mypy pylint flake8 check-manifest

build:
	rm -rf build/ dist/ src/colorviews.egg-info/
	python3 setup.py sdist bdist_wheel

purge_cache:
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
