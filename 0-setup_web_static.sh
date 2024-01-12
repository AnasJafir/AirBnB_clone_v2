#!/usr/bin/env bash
# Check if Nginx is installed
if ! command -v nginx &> /dev/null
then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

# Create directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake html file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ to ubuntu user & group
sudo chown -R ubuntu:ubuntu /data/

# Configure the Nginx configuration to serve content of /data/web_static/current/ to hbnb_static
sudo sed -i "51 i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

