# fullstack-test-nina
Template repository for fullstack web developers at Super NINA.

# Challenge
As part of the selection process, we would like you to:

1. [Backend] Implement a missing feature that returns all the complaints from a given user. This will measure your ability in developing new features in an on-going project.
2. [Backend] Implement a filtering functionality to the get_complaints route (```/complaints```) allowing it to return only the complaints where the field ```date``` is in between the fields ```from_date``` and ```to_date```, passed through query parameters.
2. [Backend] Solve any bugs or problems you encounter in the template. We deliberately introduced some simples bugs that will measure your ability in debugging and problem solving.
3. [Frontend] Build a small Angular application that makes a REST API call to a provided endpoint. This will allow us to evaluate your understanding of Angular, HTTP requests, and working with external APIs.
4. [Frontend] Follow the design provided by our designer. This will allow us to measure how well you work with a designer on the team.
5. [Frontend] Implement routing for the 3 pages needed for Angular Application.

Your submission will be tested using:
- Python 3.11
- Node 18.19
- Angular CLI 17.3

<!-- - Connect to a web socket and display real time notifications as pop-ups. This will allow us to evaluate your understandings of websockets and data streaming. -->

Anything more than that such as useful documentation, automated tests or the creation of docker containers will be counted as bonus features and **will** highlight your submission. Remember to explicitly point how to run your additions if you introduced them!

**Not being able to complete all the assignments does not mean failing the challenge! Try to do as much as possible and send us your submission before the deadline even if it's incomplete!**

After the test, even if you aren't selected, the devs at Super NINA will do their best to give you honest feedback and guide you to future improvements.

When you have completed the test, please submit to us (as a response to the email informing you were selected for the tech challenge):

- A link to the code repository (e.g. GitHub, GitLab, etc.) where we can view your code.


- A brief explanation of your decisions, any challenges you encountered, and how you overcame them (in regard to the challenge).

We look forward to seeing your work!

# Backend
## Requirements
- Python 3.11+

## Installing dependencies
From the root of the project, run:
```sh
pip install -r back/requirements.txt
```

## Running server
From the root of the project, run:
```sh
fastapi dev back/app.py
```

# Frontend
## Requirements
-

## Installing dependencies
From the root of the project, run:
```sh

```

## Running frontend
From the root of the project, run:
```sh

```