all: run

env: requirements.txt
	rm -rf env
	virtualenv -p python3 env
	env/bin/pip install -r requirements.txt

.PHONY: run
run: env
	FLASK_APP=app.py \
	FLASK_DEBUG=1 \
	env/bin/flask run

.PHONY: clean
clean:
	rm -rf env
