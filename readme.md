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

`python -m venv env`
`env\Scripts\activate.bat`
