@smoke_test
Feature: Search feature

  Scenario Outline: Validating the search feature
    Given I have navigate to google.com
    When I validate the page title
    Then I enter text "<Title>"
    And I click the search button
    Examples:
      | Title       |
      | BDD         |
      | TDD         |

