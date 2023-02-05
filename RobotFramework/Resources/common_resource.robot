*** Settings ***
Documentation     A resource file with reusable keywords and variables.

Library           ../../TestFramework/Libraries/TestFixture.py
Library           ../../TestFramework/Libraries/Modules/excel_reader_writer.py
Library           Collections


*** Variables ***
${DEFAULT TIME OUT VALUE}       60                                                                          # Webdriver default time out value. editable. should be greater than 0, Can't be empty
${URL}                          https://www.google.com/                                                             # Application URL.
${VALID USERNAME}               -----------------                                                        # Valid user name.
${VALID PASSWORD}               -----------------                                                                # Valid password.
${BROWSER NAME}                 Chrome                                                                      # Browser name.
${SCREENSHOT DIRECTORY}         ${EMPTY}                                                                    # Screenshot directory, selected based on project output directory.
${IMAGE PATH}                   ${EMPTY}                                                                    # Image path. is returned from test framework.
${LOGIN STATUS}                 ${EMPTY}                                                                    # Login status
${TEST DATA FILE PATH}          ${EXECDIR}\\RobotFramework\\Resources\\ExternalDataSource\\test_data_source.xlsx       # Project test data source file path.

*** Keywords ***
Validate SetUp
    Set execution directory         ${EXECDIR}
    log     ${EXECDIR}
    Setup    ${BROWSER NAME}
    set time out value      ${DEFAULT TIME OUT VALUE}
    Goto    ${URL}

Validate Suite Teardown
    teardown

Log Screenshot
    ${SCREENSHOT DIRECTORY} =   get variable value      ${OUTPUT DIR}
    ${IMAGE PATH} =    capture screenshot     ${SCREENSHOT DIRECTORY}
    Log    <img src="${IMAGE PATH}">    HTML

Read Test Data From Excel Sheet
    [Arguments]     ${TEST DATA FILE PATH}      ${SHEET NAME}
    ${TEST DATA DICTIONARY} =       read test data      ${TEST DATA FILE PATH}      ${SHEET NAME}
    log     ${TEST DATA DICTIONARY}
    return from keyword     ${TEST DATA DICTIONARY}

Get Test Data Value From Excel Sheet
    [Arguments]     ${TEST DATA DICTIONARY}     ${KEYWORD}
    ${RETRIEVED SPECIFIC VALUE FROM EXCEL} =    get from dictionary     ${TEST DATA DICTIONARY}     ${KEYWORD}
    return from keyword     ${RETRIEVED SPECIFIC VALUE FROM EXCEL}
