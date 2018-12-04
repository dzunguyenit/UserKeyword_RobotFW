*** Settings ***
Library           SeleniumLibrary
Library           UserKeywords.py

*** Test Cases ***
testCase1
    ${resultTwo}=    Gettwowords    Nguyen    Huynh     Thanh    Vu
    log    ${resultTwo}
