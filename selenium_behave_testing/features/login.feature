Feature: Logging in
    As a user I want to login to my account
    
    # TC_03
    Scenario Outline: Tests if routing will take to correct html page upon success/failure
        Given I am on the home page
        When I put my username: "<username>"
        When I put my password: "<password>"
        When I click on the login button
        Then I will be on the "<location>" page

        Examples:
            | username  | password      | location  | 
            | employee  | Password123   | Account   |
            | adv123    | pass222       | Home      |

    # TC_02
    Scenario Outline: Tests verification of login details (Behave) 
        Given I am on the home page
        When I put my username: "<username>"
        When I put my password: "<password>"
        When I click on the login button
        Then I will be shown the error message: "<err_msg>"

        Examples:
            | username  | password      | err_msg                                                       |
            | Andy      | empty         | Make sure your username and password is 1 to 30 letters long! |
            | empty     | Password123   | Make sure your username and password is 1 to 30 letters long! |
            | empty     | empty         | Make sure your username and password is 1 to 30 letters long! |   
            | fake_user | fake_pw       | User doesn't exist!                                           |
       