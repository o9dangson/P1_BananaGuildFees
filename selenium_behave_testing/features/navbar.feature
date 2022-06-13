Feature: Navbar
    As a user, I am able to use the navbar to traverse my account.
    
    # TC_11
    Scenario Outline: Tests navbar logout
        Given I am on the landing page
        When I put in my username: "<username>"
        When I put in my password: "<password>"
        When I click on the login button once
        When I click on the logout button once
        Then I should be on the home page

        Examples:
            | username  | password      | 
            | employee  | Password123   | 
            | manager   | Password123   |
    
    Scenario Outline: Tests navbar options
        Given I am on the landing page
        When I put in my username: "<username>"
        When I put in my password: "<password>"
        When I click on the login button once
        Then I should see this "<option>"

        Examples:
            | username  | password      | option                    |
            | employee  | Password123   | Home                      |
            | employee  | Password123   | Log Out                   |
            | manager   | Password123   | Home                      |
            | manager   | Password123   | Manage Pending Requests   |
            | manager   | Password123   | Log Out                   |

    Scenario Outline: Tests navbar functions
        Given I am on the landing page
        When I put in my username: "<username>"
        When I put in my password: "<password>"
        When I click on the login button once
        Then I should see the relevant pages of "<option>"

        Examples:
            | username  | password      | option    |
            | employee  | Password123   | Home      |
            | employee  | Password123   | Log Out   |
            | manager   | Password123   | Home      |
            | manager   | Password123   | Manage    |
            | manager   | Password123   | Log Out   |
    