Feature: Managing Requests
    As a manager, I am able to approve/reject ongoing requests that aren't mine.

    # TC_10
    # Will expand when have more guild masters to scenario outline
    Scenario: Tests if scripts populates html elements correctly
        Given I am on the Account page
        When I click on the Manage Pending Request Page
        Then I should see all requests that aren't mine

