echo "Build the project - install the packages"
python3.9 -m pip install -r requirements.txt
echo "Making Migrations"
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput
echo "Collecting Static Files"
python3.9 manage.py collectstatic --noinput --clear
