# Turbo Complete Data 📀

Welcome to the documentation for the repository in charge of data for the Turbo complete  AI project. This documentation provides information on how to set up, run, and contribute to the frontend codebase.

📜 Table of Contents

- [Introduction](#introduction)
- [Built With](#build-with)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick_start)
- [Environment Configuration](#environment-configuration)
- [Run the Application](#run-the-application)
- [Contributing](#contributing)
- [To Improve](#to-improve)
- [Feedback](#feedback)


## Introduction
This project is the data part of the AI Turbo complete 🚀 application. It interacts with the Ebay API and MongoDB  to provide data to be used by the algorithms of the project.

## Built With
- Python 3
- Python libraries such as : 

- [Ebay_rest](https://github.com/matecsaj/ebay_rest)
- [Beautifulsoup](https://pypi.org/project/beautifulsoup4/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Pymongo](https://pymongo.readthedocs.io/en/stable/tutorial.html)


## Prerequisites
Before running the project, ensure you have the following installed on your system:

Python3: The programming language used for the project.
Pip: The package installer for Python.
Virtualenv: A tool for creating isolated Python environments.

## Quick Start

1. Clone the repository

2. Navigate to the project directory

3.Install dependencies

```
pip install -r requirements.txt
```

4. Set ebay_rest
https://github.com/matecsaj/ebay_rest

5. Create an account on MongoDB cloud


## Environment Configuration
```
Create a .env.local file in the project root and configure necessary environment variables fot EBAY API, MONGODB

MONGODBCLIENT=***your_url***
APPLICATION=production_1
USER=production_1
HEADER=US
```

## Run the Application

1. Go to app/api

2. run the API
```
python3 main.py
```


## Contributing
We welcome contributions! To contribute to the project, follow these steps:

Fork the repository.
Create a new branch: git checkout -b feature/your-feature-name.
Make your changes and commit them: git commit -m 'Add some feature'.
Push to the branch: git push origin feature/your-feature-name.
Submit a pull request.


## To improve
Here are some areas for improvement:

Tests API
Implement Docker for easier application access.
Feel free to contribute and help make Turbo complete 🚀 even better!

## Feedback
