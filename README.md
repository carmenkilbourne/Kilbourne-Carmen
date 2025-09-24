 # Technical Challenge – Python Junior Backend Developer
 ## Description
 This project implements a CRUD(Create, Read, Update, Delete) structure for subscriptions stored in a list.

## Steps taken
 1. Set the environment that i'm going to be working in, in this case 
 i'm using flask.
 2. Created mock data to see if my endpoint works correctly.
 3. Created my post endpoint and tested it in postman.
 4. Created a list to manage all the subscriptions and a autoincremented id.
 5. Implemented the minimal validations.
 6. Restricted the allowed values of plan.
 7. Added the method to get subscription by id.
 8. Added methods put and delete.
 9. Test functions in main with pytest.
## Decisions made
I choose to put my subscription in a list instead of other structures like a dictionary or a class because its a structure that i find easy to iterate over and its good when there's a small amount of data.
## 🏁 Running the Project
For running this project you need to have installed phyton.
To install dependencies 
```
pip install -r requirements.txt
```
```
flask run # For Flask
```
to run tests use this command:
 ```
 pytest .\test_main.py
 ```

