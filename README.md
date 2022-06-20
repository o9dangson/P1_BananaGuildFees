# P1_BananaGuildFees

`BananaGuildFees` is an online service that allows existing adventurers and guildmasters of the Banana Guild to log into their respective accounts and submit reimbursement requests due to the dangers and costs of their profession. 

As an adventurer, you will be able to see previous requests as well as cancel `Pending` ones, so you can keep your banking up to date.

Guild masters need not worry, you will be able to do everything adventurers can and more! Using the special manage page only privileged members have access too, you can `accept or reject` requests from adventurers. Only the requests that aren't outlandish will make it through.


# Technologies
`BananaGuildFees` was built using the Flask web framework for the server-side interactions. Flask would also do session handling for logged in users.

Communication with the database was done using the psycopg2 package. 
The database was implemented using AWS RDS with PostGreSQL RDBMS.

Client-side interactions were implemented using a combination of JavaScript, HTML, and Bootstrap. JavaScript would interact with the server and retrieve data using the Fecth API.

Unit testing was done through the pytest package. Integration testing was implemented using Postman API test. Acceptence Testing was done with the behave package which uses Selenium WebDrivers and Gherkin syntax.

# Install
## Prerequsites
In order to run Banana Guild Fees you must have the follwing technology installed:
- Python 3.9.12 or higher
    - pip required
- Git or Github account
- Command Line Interface

---
## Steps
1. Install pip package `virtualenv`
    ```
    pip install virtualenv
    ```

2. Clone this repository to your desired directory
    ```
    git clone https://github.com/o9dangson/P1_BananaGuildWoes.git
    ```
    
3. Create virtual environment in the same directory
    ```
    virtualenv venv
    ```
    
4. Activate virtual environment
    ```
    source venv/Scripts/activate
    ```
    
5. Install requirements
    ```
    pip install -r requirements.txt
    ```
    
6. Run the main app.py file
   ```
   python app.py
   ```

   - Observe on your local machine: `localhost:5000`
   
### Testing
- To run pytest use the following command in the root directory:
    ```
    pytest
    ```

- To run the `behave` tests:
    ```
    cd selenium_behave_testing
    behave
    ```

# Link to Test Documents
[Test Report](https://docs.google.com/spreadsheets/d/1GN4pi0J25HsIq3dvJf-uyJMKNE71tpWLC1wXQtiCkQA/edit?usp=sharing)

[RTM](https://docs.google.com/spreadsheets/d/14Z-w8EPUCjwkrnTl1y7GtZ0ek5Ullm5OVsrX_f4RUJk/edit?usp=sharing)

[User Stories](https://trello.com/b/2JVaS5aB/kanban-p1)

[All Other Test Documentation](/documentation)
