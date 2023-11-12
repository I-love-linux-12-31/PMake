## PMake
**PMake** - my make implementation on python3 (see task 4 on: https://github.com/true-grue/kisscm/blob/main/pract/homework.md)

### Dependencies
* Python3
* PyYAML
* sqlite3
* *Make (for installation using Makefile)


App config and db file located at: ~/.PMake/

#### Installation
<code>$ make install</code> - to install application. Logout or reboot required to run app using <code>$ pmake</code> command

<code>$ make uninstall</code> - for removing application WITHOUT db and config files

<code>$ make uninstall-full</code> - for removing application with ALL data files
