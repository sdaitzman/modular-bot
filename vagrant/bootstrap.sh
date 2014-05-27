#!/usr/bin/env bash

# CC AS NC 4.0 License (http://creativecommons.org/licenses/by-sa/4.0/legalcode)
# Sam Daitzman - May 26, 2014 - http://github.com/sdaitzman

# update software repositories
apt-get update

# install, assuming yes, node and npm and fish-shell and preload and htop and nginx
apt-get install -y node npm fish preload htop nginx

# change default user shell for user vagrant to fish-shell
chsh -s /usr/bin/fish vagrant