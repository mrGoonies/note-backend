setup:
	python3 -m venv venv
	. venv/bin/activate; pip install -r requirements.txt

run-local:
	uvicorn app.main:app --reload