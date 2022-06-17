Feature: All behaviour combined
    As an adventurer I can create a request so it can be accepted by a guild master

    Scenario: Put in bad login in
        Given I am on the starting page
        When I input an incorrect username
        When I input an incorrect password
        When I click the login button
        Then I should see an error message for logging in

    Scenario: Adventurer logging in
        Given I am on the starting page
        When I input my adv username
        When I input my adv password
        When I click the login button
        Then I should be on the account page

    Scenario: Makes bad request
        Given I am currently on the account page
        When I click the add request button
        When I put in an incorrect amount
        When I put in a description
        When I press the create button
        Then I should see an error for invalid input

    Scenario: Makes good request
        Given I am currently on the account page
        When I put in an amount
        When I put in a description
        When I press the create button
        Then I should have a new pending request

    Scenario: Cancels request
        Given I am currently on the account page
        When I click on the cancel button for the request I just made
        When I press the logout button in the navbar
        Then I should be on the login page

    Scenario: Guild Master making request and approving a request
        Given I am on the starting page
        When I input my gm username
        When I input my gm password
        When I click the login button
        When I press the Manage Pending Request option in the navbar
        When I press the accept button on a request
        When I press the logout button in the navbar
        Then I should be on the login page
