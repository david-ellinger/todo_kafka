# Purpose

- Integrate with Todoist API
- Add proxy commands
  - Add task
  - Read task
- Command will produce an event
  - Avro schema
- One consumer will call out to todoist api
- One consumer will save event to sqlite db

## Alternative
- Setup endpoint for todoist webhooks
- Convert todo to todo.txt universal format
- Store in sqlite
   - eventually postgres

# Commands

## Package
`task add TASK_DESCRIPTION`
`task 1 delete`
`task 1 done`
`task 1 edit TASK_DESCRIPTION`
`task list --todoist`
`task list --db`

## Local Development
`python -m venv env`
`env\Scripts\activate.bat`

Install script locally
`pip install --editable .`

### Docker
`docker-compose build`
`docker-compose run --service-ports kafdrop`

# References
- https://dzone.com/articles/introduction-to-event-streaming-with-kafka-and-kaf-1
