#!/bin/bash

echo $PATH | grep -q $1 && echo "Already in PATH!" || (echo 'export PATH=$PATH:'$1 >> "$HOME/.bash_profile" && echo "To apply changes logout or reboot computer.")