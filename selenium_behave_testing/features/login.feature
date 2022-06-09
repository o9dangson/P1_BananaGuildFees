# TC_03
Feature: Logging in
    As a user I want to login to my account

    Scenario Outline:
        Given I am on the home page
        When I put my username: "<username>"
        When I put my password: "<password>"
        When I click on the login button
        Then I will be on the "<location>" page

        Examples:
            | username  | password      | location  |
            | employee  | Password123   | Account   |
            | adv123    | pass222       | Home      |