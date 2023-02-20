# build_files.sh
echo "starting to upgrade pip"
pip install --upgrade pip
echo "using pip to unstall from requirements.txt baby"
pip install -r requirements.txt
echo "stating to arrange static files"
python manage.py collectstatic --noinput
