# Created by abhil at 25-02-2024
Feature: Verify if Books are added and deleted using library API

    @library
    Scenario: Verify AddBook API functionality
      Given the book details which needs to be added to library
      When  we execute the AddBook PostAPI methode
      Then book is successfully added
      And status code of response should be 200

    @library
    Scenario Outline: Verify AddBook API functionality
      Given the book details with <isbn> and <aisle>
      When  we execute the AddBook PostAPI methode
      Then book is successfully added
      Examples:
        |isbn |aisle |
        |uigq | 1022 |
        |yqyo | 4706 |