## Download necessary files 


* There is `requirements.txt` file, which we could use to put the dependent packages for the project in (for pip).
* `pyproject.toml` .. (for poetry).



> We could use pip freeze > requirements.txt to move all current packages used in current environment to the requirements file.

## Difference between pip and poetry

* `pip` basic package installer that simply downloads and installs packages, leaving virtual environment and dependency management to you
* `poetry` has built in VE, and can detect current VE.
* Has dependency management.
* `poetry` is a comprehensive project management tool that automatically resolves dependency conflicts.
## Apply packages 

* To download the packages from `requirements.txt`, use `pip install -r requirements.txt`.
* For poetry: 

    1) Use `poetry init` to generate `pyproject.toml` file. 
    2) `poetry run python file.py` to run python file inside the env.
    3) To install packages inside the `pyproject.toml` use `poetry install`
    4) To add packages to current env use `poetry add <package name>`



> To check for a package existent or not in the current env use `importlib.util.find_spec(package_name)`
