@sanity
Feature: Search feature

  Background:
    Given I have navigate to google.com

  Scenario: Validating search feature
    When I validate the page title
    Then I enter text "hello selenium"
    And I click the search button


  Scenario: Validating search  with new text
    When I validate the page title
    Then I enter text "hello behave"
    And I click the search button




