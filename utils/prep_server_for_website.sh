#!/usr/bin/bash
sudo apt-get -y update
sudo apt-get -y install mysql-server postfix supervisor nginx git
sudo apt-get -y install python3-venv

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

pip install gunicorn pymysql

# python3 -c "import uuid; print(uuid.uuid4().hex)"

SECRET_KEY=<put-something-here>
MAIL_SERVER=localhost
MAIL_PORT=25
DATABASE_URL=mysql+pymysql://teacherprints:<db-password>@localhost:3306/microblog
MS_TRANSLATOR_KEY=<your-translator-key-here>

echo "export FLASK_APP=tp-website.py" >> ~/.profile

# git clone https://github.com/TSSlade/teacherprints
# cd tp_website
# git checkout prod



# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux