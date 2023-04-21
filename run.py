import subprocess

# activate the virtual environment
subprocess.run("venv\\Scripts\\activate.bat", shell=True)

# install the required packages
subprocess.run("pip install -r requirements.txt", shell=True)

# start the Django server
subprocess.run("python manage.py runserver", shell=True)
