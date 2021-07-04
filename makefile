test :
	python3 -m pytest; mypy --exclude='tests/integration_tests/*' .
