set -o errexit
pip install -r requiremensts.txt


python manage.py collectstatic --no-input
python manage.py migrate