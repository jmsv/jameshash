install:
	python setup.py install

test tests:
	@python tests.py

clean:
	@rm -f *.pyc */*.pyc
	@rm -rf jameshash.egg-info build dist
	@rm -rf */__pycache__

