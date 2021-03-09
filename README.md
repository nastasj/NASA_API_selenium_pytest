##  How to run tests

```
$ git clone https://github.com/nastasj/API_NASA_selenium_pytest.git
$ cd API_NASA_selenium_pytest
Create and activate virtual environment as you usually do
$ pip install -r requirements.txt
$ pytest
``` 

##  How to run tests with Allure report

```
$ pytest --alluredir=allure-results
$ allure generate allure-results
$ allure open
``` 
![allure](https://user-images.githubusercontent.com/78635647/110435153-b3e46580-80c3-11eb-9648-381852bad345.png)
