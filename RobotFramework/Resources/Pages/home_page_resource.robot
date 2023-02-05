*** Settings ***
Documentation   Home Page Resource File With All Necessary Keywords.

Resource        ../common_resource.robot

Library     ../../../TestFramework/Libraries/RobotTests/Home.py
Library         Collections

*** Variables ***
${STATUS}                                            False

*** Keywords ***
Verify Search With Specific Keyword
    [Arguments]     ${KEYWORD}
    ${STATUS} =     search with specific keyword     ${KEYWORD}
    should be true      ${STATUS}      Unable to search ${KEYWORD} keyword
    [Teardown]      run keyword if    '${STATUS}'=='False'    Log Screenshot