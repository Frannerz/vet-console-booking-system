# Assignment-4-CFG
## API architects: From Requests to Reality

### Contributors:
- Fran (github.com/Frannerz)
- Eve (github.com/EveRefi)
- Kate (github.com/sonderserendipity)
- Norah (github.com/sialf)

### The project:
(What the project does and why it's is useful)
- This is a vetinary practice booking system
- It allows vet clinics to view and amend appointments  
- It also allows them access to patient info

### Setup:
1. Clone the repo using `git clone url-addess`
2. Navigate `cd repository-name`
3. Activate virtual environment `source virtual-environment/bin/activate`
4. Use the requirements.txt file to install the dependencies: `pip install -r requirements.txt`
- A requirements.txt file in Python projects is used to manage package dependencies.
- It contains a list of pip-installable packages with their versions, ensuring consistent environments across different setups.
- You can generate it using `pip freeze` and install from it using `pip install -r requirements.txt`
5. Move into the venv folder `cd virtual-environment`
6. Create config.py file:
- Your file should look something like this, depending on your db settings:
```
mysql_settings = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR PASSWORD",
    "db": "VetSurgery",
}
```
7. Create .gitignore file and ensure it contains correct files:
Add these files:
```
/lib/
config.py
```
*(A .gitignore file specifies the untracked files that Git should ignore. Files listed in .gitignore won't show up in unstaged changes or be added to your repository when you use git add commands.)*

8. Create the database
- Use vet-surgery.sql to create your db in mysql

### Help on db interaction:
- https://medium.com/@connect.hashblock/creating-an-api-in-flask-with-mysql-a-step-by-step-guide-446f08722057
- https://hevodata.com/learn/flask-mysql/

### Screenshots for question 1
- Checking the status
- Creating a branch
- Adding files to a branch
- Adding commits with meaningful messages Opening a pull request
- Merging and deploying to main branch
- If needed, take screenshots of the process and add to your README file.
**Evidence:**
<img src="https://github.com/Frannerz/Assignment-4-CFG/assets/124707247/912ad325-5f2c-4e20-b4db-5dc511904547" alt="Alt text" width="400">
<img src="https://github.com/Frannerz/Assignment-4-CFG/assets/124707247/a8e718eb-124c-42d3-a6eb-60a286c5d4d0" alt="Alt text" width="400">



### Links to previous projects:
