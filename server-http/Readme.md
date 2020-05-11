# Manage packages Python

When I say Python **environment**, I mean: The ecosystem consisting of your particular installed version of python, plus all the third-party packages (“libraries”) it can access (and their precise versions). Every time you `$ pip install`something, you are expanding your python environment, giving it access to packages that are not part of the [Python standard library](https://docs.python.org/3/library/index.html).

If you `$ pip install` a bunch of stuff outside of a **virtual environment**, then you are adding to your “base” or “root” or “system” python environment. 

However, working exclusively in your base environment. When we want to share our Python code **not everyone has the same packages** (and versions of those packages) installed.



This is where a **requirements.txt** file comes into play. This file can be created with **Pip Freeze**:

`cd myrpject`

`pip freeze > requirements.txt`

Then right now, we can install all cheking dependiencies with the following command:

`pip install -r requirements.txt` 

There is a problem with the command aboce,  `pip` didn't include a way to isolate packages from each other. We might work on apps that use different versions of the same libraries, so we needed a way to enable that.

It's resolve with **Pipenv**, it comes to our rescue!

Firts, install pipenv:

```
pip install --user pipenv
```

So, Install dependencies (pipenv automatically detect `requirements.txt`and solve the dependencies)

```
cd myproject
pipenv install requests
```

Finally, `Pipfile` and `Pipfile.lock` should be created

- Pipfile: list of all installed packages
- Pipfile.lock: maintain a proper dependencies and sub packages with version



Now, run your python script (Installed packages are available when you use `pipenv run`)

```
$ pipenv run python [YOUR PYTHON MAIN SCRIPT]
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
✔ Success! 
Updated Pipfile.lock (980232)!
Installing dependencies from Pipfile.lock (980232)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 73/73 — 00:01:22
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```

 ## Note

If you are using Python3 then you must change the name **pip** for **pip3**.