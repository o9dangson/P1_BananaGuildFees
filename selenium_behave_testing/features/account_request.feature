Feature: Request Manipulation
    As a user, I am able to see ongoing and previous requests
    As a user, I am able to see total spent on requests

    # TC_09: Tests if scripts populates html elements correctly
    Scenario Outline: Observing all requests
        Given I am logged in with "<username>"
        Then I should see all requests of this user

        Examples:
            | username  |
            | employee  |
            | manager   |

    Scenario Outline: Observing total request amount
        Given I am logged in with "<username>"
        Then I should see total request amount of this user     
        
        Examples:
            | username  |  
            | employee  |       
            | manager   |        

    Scenario Outline: Observing canceling request
        Given I am logged in with "<username>"
        When I create a brand new req
        When I cancel a newly created request
        Then I should not see the request anymore

        Examples:
            | username  |
            | employee  |