LocalStorage -up--|> Singleton
## Example of selenium test framework base on pytest in functional approach
---
### Structure of project
    |-- .env
    |-- .gitignore
    |-- README.md
    |-- conftest.py
    |-- requirements.txt
    |-- core
    |   |-- __init__.pyw
    |   |-- locator.py
    |   |-- page_object_singleton.py
    |   |-- singleton.py
    |   |-- config
    |   |   |-- __init__.py
    |   |   |-- config.py
    |   |   |-- db_config.py
    |   |   |-- test_rale_config.py
    |   |-- domain
    |   |   |-- result.py
    |   |-- infrastructure
    |       |-- __init__.py
    |       |-- cookie.py
    |       |-- local_storage.py
    |       |-- bin
    |       |   |-- chromedriver
    |       |-- models
    |       |   |-- __init__.py
    |       |   |-- base_model.py
    |       |   |-- test_result.py
    |       |-- repositories
    |           |-- base_repository.py
    |           |-- test_result_repository.py
    |-- pages
    |   |-- __init__.py
    |   |-- c_sharp_cource_page.py
    |   |-- base_page
    |   |   |-- __init__.py
    |   |   |-- base_page.py
    |   |   |-- base_page_locators.py
    |   |   |-- header.py
    |   |-- dashboard_page
    |       |-- __init__.py
    |       |-- dashboard_locators_collection.py
    |       |-- dashboard_page.py
    |-- tests
        |-- test_csharp_course.py
---
### Setup project
1. Download compatible version of chrome driver
2. Rename chrome driver to chromedriver and move into core/infrastructure/bin forlder
3. Install postgresql database and create db with name same as in config /core/config/db_config.py
4. Create table 'test_result' same as provided model in core/infrastructure/models/test_result.py
5. Install dependencies:
```
pip install -r requirements.txt
```
6. Run tests with command:
```
pytest .
```
# Architecture diagram of project WIP

![diagram](/docs/static/hierarchy.png)