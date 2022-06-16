Feature: Create Request 
    As a user, I am able to create a new reimbursement request

    Scenario: Successful request creation
        Given I am logged in as an adventerer
        When I click on the add request button
        When I input an amount
        When I input a description 
        When I click the create button
        Then My request should show up in pending requests

    Scenario Outline: Failing request creation
        Given I am logged in as an adventerer
        When I click on the add request button
        When I input an "<amount>"
        When I input a "<description>"
        When I click the create button
        Then I should see an error message

        Examples:
            | amount        | description                                                                                                                           |
            | empty         | This is something                                                                                                                     |
            | 200           | empty                                                                                                                                 |
            | empty         | empty                                                                                                                                 |
            | ldasdald      | This is a description                                                                                                                 |
            | 200000        | Horses                                                                                                                                |
            | 0             | Hello                                                                                                                                 |
            | 400           | This is a description This is a description This is a description This is a description This is a description This is a description   |
