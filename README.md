# PetstoreApiTests

Tests for https://petstore.swagger.io/v2
### functional_tests contains functional tests cases 
For parallel test run:
To install:
#### pip install pytest_xdist
To run:
#### pytest -n NUM
For default report generation:
To install:
#### pip install pytest-html
To generate to report.html:
#### pytest --html=report.html
For allure report generation:
To install:
#### pip install allure-pytest
To generate to allureres:
#### pytest -n 5 --alluredir allureres
#### allure serve allureres
