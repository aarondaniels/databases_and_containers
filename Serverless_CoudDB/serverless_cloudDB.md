# Serverless Cloud Database
Google Firebase is the go-to serverless cloud database. To start working with Firebase, navigate to the Firebase website. You should be automatically logged in with your Google profile. If you are not logged in, please create a Google profile and log in.

To start creating a new project, select “Go to console” and then select “Create a project”.

Next, name your project, e.g., PCDE, then select “Continue”.

On the next page, select “Continue”, and then select the “Default Account for Firebase”. Finally, select “Create Project”.

Once the project has been created, you will need permissions to write from Python to your database. To set the permissions, select “Project Overview”, and then select “Project Settings”.

Navigate to “Service Accounts” and then select “Python”.

To generate your own private key that will allow you to connect to the Firebase database, select “Generate new private key”.

After you confirm you want to generate a new private key, a JSON file will be automatically downloaded on your machine. Move that file to the same location of the fire.py file you downloaded at the beginning of this mini-lesson.

Rename the downloaded file “serviceAccountKey.json”.

On the Firebase website, select “Realtime Database” in the left panel, and then select “Create Database”. Choose your time zone and select the option “Start in locked mode”.

Copy the Realtime database URL.

Open the `fire.py` file in VS Code. Update the `databaseURL` field with the URL you copied in the previous step.

From a Terminal window, install the necessary Firebase libraries by typing the following command:

`pip3 install firebase_admin`

Once this is complete, run the following command in your Terminal window:

`python3 fire.py`

Now, if you navigate to your Realtime database in Firebase, you should see the updated database.

In short, as a serverless cloud database, Firebase allows you to read, write, and store databases on a cloud using simple Python code.