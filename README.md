# CleanCode-Projet-API

## Pre-requisite 

Before trying to install this API, you have to install Docker and Python 3.

## Installation

First create a virtual env by using this command :  
```
python3 -m venv venv
```

Then ou have to activate the virtual env :
```
source venv/bin/activate
```

After this install all the dependencies in the virtual env :
```
pip install -r requirements.txt
```

And to start the API use this command :
```
uvicorn app:app --reload
```