# Created by abhil at 27-02-2024
Feature: Github API Validation
  # Enter feature description here

  @github
  Scenario: Session management check
    Given I have github auth credential
    When I hit getrepo API of github
    Then status code of response should be 200
    # Enter steps here