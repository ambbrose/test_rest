# build_files.sh
echo "starting to upgrade pip"
pip install --upgrade pip
echo "using pip to install the packages"
pip install asgiref==3.6.0
pip install backports.zoneinfo==0.2.1
pip install dj-database-url==1.2.0
pip install Django==4.1.3
pip install djangorestframework==3.14.0
pip install Pillow==9.4.0
pip install python-decouple==3.7
pip install pytz==2022.7.1
pip install sqlparse==0.4.3
pip install tzdata==2022.7
echo "stating to arrange static files"
python manage.py collectstatic --noinput
