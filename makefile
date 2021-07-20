test :
	python3 -m pytest -vv; mypy --exclude='tests/integration_tests/*' .
