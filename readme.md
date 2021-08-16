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

## Schema
`todo` - Show Help\
`todo --help` - Show Help\
`todo db --help` Show DB commands\
`todo db init` - Add mock data\
`todo db drop` - Remove mock data\
`todo db status` - List all tasks from db - Name | Project | # of Subtasks
`todo db backup` - Backup db (??)
`todo status` - List all open tasks - Name | Project | # of Subtasks and shows the Provider (TodoistProvider default)
`todo sync **TODOIST_TASK_ID**` - Adds todoist task to local db
`todo add *description string*` - Adds task to todoist. Default behavior
`todo add --description *descrition string*` - Same behavior as above.
`todo edit --task *todoist_task_id* --description "new description"` - Edit todoist task w/ new description
## Local Development
`python -m venv env`
`env\Scripts\activate.bat`

Install script locally
`pip install --editable .`

### Docker
Kafdrop URL - http://localhost:9000/

`docker-compose build`

`docker-compose run --service-ports todo initdb`

`docker-compose run --service-ports todo add`
#### Consumer
`docker-compose run --service-ports todo-consumer`





# References
- https://dzone.com/articles/introduction-to-event-streaming-with-kafka-and-kaf-1
