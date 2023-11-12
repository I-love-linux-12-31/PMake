INSTALL_ROOT = $(HOME)"/.local/bin"
install:
	if [ ! -d $(INSTALL_ROOT)/PMakeLib ]; then (mkdir $(INSTALL_ROOT)"/PMakeLib") fi;
	cp pmake.py ~/.local/bin/
	ln -s ~/.local/bin/pmake.py ~/.local/bin/pmake
	cp -r PMakeLib ~/.local/bin/PMakeLib
	if [ ! -d $(HOME)"/.PMake/" ]; then (mkdir $(HOME)"/.PMake/") fi;
	cp app_config.yaml ~/.PMake/
	cp db.sqlite3 ~/.PMake/
	# echo $PATH | grep -q $(INSTALL_ROOT) || echo 'export PATH='$(PATH)':'$(INSTALL_ROOT) >> $(HOME)"/.bash_profile"
	bash add_to_path.sh "$(INSTALL_ROOT)"

uninstall:
	rm -rf ~/.local/bin/PMakeLib
	rm -f ~/.local/bin/pmake.py
	rm -f ~/.local/bin/pmake

uninstall-full: uninstall
	rm -rf ~/.PMake/
