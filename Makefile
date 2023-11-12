install:
	mkdir ~/.local/bin/PMakeLib
	cp pmake.py ~/.local/bin/
	cp -r PMakeLib ~/.local/bin/PMakeLib
	mkdir ~/.PMake/
	cp app_config.yaml ~/.PMake/
	cp db.sqlite3 ~/.PMake/

uninstall:
	rm -rf ~/.local/bin/PMakeLib
	rm -f ~/.local/bin/pmake.py


uninstall-full: uninstall
	rm -rf ~/.PMake/
