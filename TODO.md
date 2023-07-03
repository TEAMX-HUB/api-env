# Project TODO Checklist

## Setting Up Supabase for Remote development

- create a supabase account
- locate where the URI connect key is (will use that for connections)
- set up database store for
  - USERS
    - class reps
    - adminstrators
  - BUILDINGS
    - classrooms
    - laboratories
    - staff offices
- set up storage for all attributes of Building and related entities.
- test out authentication with dumpy data and share api keys with frontend-dev

## Setting Up the project base

[Some Video for setting up Flask](https://www.youtube.com/watch?v=fsNeGqxC4PM)

- go for raw sql with parameters over ORM provided by Supabase using SQLAlchemy
- reflect on the database file generated from pgAdmin
- revise models and check all the data provided are accurately schemed
- migrate new database to Supabase locally, test and push to remote.
- set up dotenv and api keys and make sure not secrets are being pushed
- try dockerising the file

(Remember Supabase is just for storage and Authentication)
(We would have to consider where to deploy the app eventually and with Docker)

## Project Documentation

- Add docstrings to each function to make documentation easier when done witj mkdocs

## Feature Implementation Notes

### Scheduling System

- Scheduling system should be able to tell which time the semester begins, when it will end,
and which days classes occur.
- Schedules have classes which have start and end times.
- Schedules should propagate throughout the time the semester begins to the time the semester ends.
- This also means creating a whole ass google calendar feature in our app. going to be postponed surely.
