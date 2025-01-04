build:
	python ../zinny-dev/bump_version.py
	python -m build

install:
	python -m pip install --upgrade .

test:
	python -m pytest tests

clean:
	rm -rf dist/ build/ src/zinny_surveys.egg-info

testpypi:
	python -m twine upload --repository testpypi dist/*
