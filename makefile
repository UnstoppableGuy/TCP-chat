venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

run_server: venv/bin/activate
	./venv/bin/python3 server.py

run_client: venv/bin/activate
 	./venv/bin/python3 client.py


clean:
	rm -rf __pycache__
	rm -rf venv