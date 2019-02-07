SHELL=/bin/bash

all:
	@# install required dependencies
	virtualenv -p python3 env
	source env/bin/activate
	env/bin/pip3 install -r requirements.txt

clean:
	@find . -name "*.pyc" -exec rm {} \;
