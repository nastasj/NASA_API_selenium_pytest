##  How to run tests

```
$ git clone https://github.com/nastasj/API_NASA_selenium_pytest.git
$ cd API_NASA_selenium_pytest
$ virtualenv -p python3 venv   # Create virtual environment
$ source venv/bin/activate # Activate virtual environment
$ pip install -r requirements.txt
$ pytest
``` 

##  How to run tests with Allure report

```
$ pytest --alluredir=allure-results
$ allure generate allure-results
$ allure open
``` 
