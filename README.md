# My_site_Django
Build a blog with Django framework

deploy the website in AWS:

Update the system:
`sudo dnf update -y`
Install git:
`sudo dnf install git -y`
To get the repository:
`git clone https://github.com/Sharon-SHH/My_site_Django.git`
install pip:
`sudo dnf install pip -y`
install Django:
`pip install Django`
or install packages in requirement.txt
`pip install -r requirements.txt`
Make Migrations:
`python3 manage.py makemigrations`
Migrate:
`python3 manage.py migrate`
create super user:
`python3 manage.py createsuperuser`
Run on server:
`python3 manage.py runserver 0.0.0.0:8000`
