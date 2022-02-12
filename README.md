## Example of selenium test framework base on pytest in functional approach
---
### Structure of project
```
-/core
.   +/config
.   +/domain
.   -/infrastructure
.   .   +/bin  
.   .   +/models
.   .   +/repositories
.   .   cookie.py
.   .   local_storage.py
-/pages
-/tests
conftest.py
requirements.txt
```
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