*** Settings ***
Documentation     Test that the user is able to search the keyword properly

Resource          ../Resources/common_resource.robot
Resource          ../Resources/Pages/home_page_resource.robot

Suite Setup       Validate SetUp
Suite Teardown    Validate Suite Teardown

*** Variables ***
${ATTENDANCE SUB MENU}    ${EMPTY}
${TEST DATA DICTIONARY}    ${EMPTY}
${SELECT LOCATION DROPDOWN ITEM}    ${EMPTY}
${TEST DATA SHEET NAME}     TestData

*** Test Cases ***
Validate Search With Specific Keyword
    [Tags]    REGRESSION
    ${TEST DATA DICTIONARY} =        Read Test Data From Excel Sheet     ${TEST DATA FILE PATH}      ${TEST DATA SHEET NAME}
    set suite variable          ${TEST DATA DICTIONARY}
    ${ATTENDANCE SUB MENU} =      Get Test Data Value From Excel Sheet        ${TEST DATA DICTIONARY}          SEARCH KEYWORD
    set suite variable          ${ATTENDANCE SUB MENU}
    Log         ${ATTENDANCE SUB MENU}
    Verify Search With Specific Keyword       ${ATTENDANCE SUB MENU}