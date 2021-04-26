The following are the main high-level features available through the app:

Users can register and login to library.
Administrators can create, update, and delete books to library.
Standard (non-admin) users have access to a "Dashboard" (the contents of which have been left empty for this iteration of the app).
Admin users have access to an "Admin Dashboard" (the contents of which have been left empty for this iteration of the app).
Helpful error, warning and success messages help the user to navigate effectively throughout form completion stages of the app.

Steps to Run the application : 

Step 1 : Initialise the PostgreSQL database:

initdb -D PGDATA
createdb library_db
psql library_db

Step 2 : flask db upgrade

Step 3 : Running the app

source activate crud-app
pip install -r requirements.txt

Step 4 : Define the following environment variables:

export FLASK_CONFIG=development
export FLASK_APP=run.py

Step 5 : flask run