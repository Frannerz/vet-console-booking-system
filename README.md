# Assignment-4-CFG
## API architects: From Requests to Reality

### Contributors:
- Fran (github.com/Frannerz)
- Eve (github.com/EveRefi)
- Kate (github.com/sonderserendipity)
- Norah (github.com/sialf)

### The project:
- This is a vetinary practice booking system
- It allows vet clinics to view and amend appointments
- It also allows them to access and amend patient and owner information
- The run function allows them to complete multiple actions one after another, without signing in again
- Exception handline throughout allows the user to easily pinpoint where errors occur

### Setup (VS code):
1. Clone the repo using `git clone url-addess`
2. Navigate into repo `cd repository-name`
3. Activate virtual environment `source virtual-environment/bin/activate`
4. Use the requirements.txt file to install the dependencies: `pip install -r requirements.txt`
    - A requirements.txt file in Python projects is used to manage package dependencies.
    - It contains a list of pip-installable packages with their versions, ensuring consistent environments across different setups.
    - You can generate it using `pip freeze` and install from it using `pip install -r requirements.txt`
5. Move into the venv folder `cd virtual-environment`
6. Update config.py file in accordance to your MySQL set-up (see notes in file)
7. Open the `.gitignore` file and ensure it contains correct files:
Add these files:
```
/lib/
config.py
```
*(A .gitignore file specifies the untracked files that Git should ignore. Files listed in .gitignore won't show up in unstaged changes or be added to your repository when you use git add commands.)*

8. Create and populate the database
- Use vet-surgery.sql to create your db in mysql

### Running the code:
1. Run `app.py` to start the server
2. From a separate terminal run `main.py`
3. You should see a printed welcome message and a list of today's appointments
4. Next you will get a printed list of actions: **book, add, view, cancel, amend**. Enter the action you would like and follow the on-screen instructions
5. Type exit to stop the application
6. When one action is completed, you will get the opportunity to complete another

### Evidence for question 1
The images below contain evidence of:
- Checking the status
- Creating a branch
- Adding files to a branch
- Adding commits with meaningful messages 
- Opening a pull request
- Merging and deploying to main branch

#### Images:
<img src="https://github.com/Frannerz/Assignment-4-CFG/assets/124707247/912ad325-5f2c-4e20-b4db-5dc511904547" alt="Alt text" width="400">
<br>
<img src="https://github.com/Frannerz/Assignment-4-CFG/assets/124707247/a8e718eb-124c-42d3-a6eb-60a286c5d4d0" alt="Alt text" width="400">

### The API checklist:
- Implement API endpoints with appropriate functionality. &#x2713; 
- Implement one additional endpoint of your choice (can be POST or GET but with a different implementation). &#x2713;
- Implement client-side for the 3 API endpoints. &#x2713;
- Create a MySQL database with at least 1 table. &#x2713;
- Have a config file (do not leave your private information here). &#x2713;
- Have db_utils file and use exception handling. &#x2713;
- Use appropriate SQL queries to interact with the database in your Flask application, and demonstrate at least two different queries. &#x2713;
- In main.py have a run() function/call the functions to simulate the planned interaction with the API. &#x2713;
- Have correct but minimal imports per file. &#x2713;
- Document how to run your API in a markdown file including editing the config file, any installation requirements up until how to run the code and what is supposed to happen. &#x2713;
- Submit in GitHub as a Pull Request. &#x2713;
