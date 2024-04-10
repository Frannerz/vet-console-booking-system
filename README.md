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
4. Install the dependencies: `pip install -r requirements.txt`
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

8. Create the database
- Use vet-surgery.sql to create your db in mysql

### Help on db interaction:
- https://medium.com/@connect.hashblock/creating-an-api-in-flask-with-mysql-a-step-by-step-guide-446f08722057
- https://hevodata.com/learn/flask-mysql/
( Add details on project setup, how users can get started, where users can get help)

### Screenshots
- Checking the status
- Creating a branch
- Adding files to a branch
- Adding commits with meaningful messages Opening a pull request
- Merging and deploying to main branch
- If needed, take screenshots of the process and add to your README file.


### Links to previous projects:
