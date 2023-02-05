@ECHO ON

:: Get the datetime in a format. The report folder will be generated based on time stamp.
SET DATETIME=%date%_%time%
SET DATETIME=%DATETIME: =_%
SET DATETIME=%DATETIME::=%
SET DATETIME=%DATETIME:/=_%
SET DATETIME=%DATETIME:.=_%
:: Test runner bat file.

SET DEFAULT_TIME_OUT_VALUE=60
SET BROWSER=Chrome
SET URL=https://www.google.com/
SET TEST_SUITE=./RobotFramework/Tests/
SET REPORT_PATH=./TestReports/

:: Please, do not update the below command
CALL robot --pythonpath ./ --variable "BROWSER NAME":%BROWSER% --variable "URL":%URL%  -d %REPORT_PATH%/%DATETIME%  %TEST_SUITE%

PAUSE