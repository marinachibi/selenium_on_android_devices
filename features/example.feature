Feature: Search on Google

Scenario: Test Login
  Given I go to google home page
  Then I search for a dog
  And I click on google search button
  Then I should see a search for dogs
