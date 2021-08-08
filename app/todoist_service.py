import todoist
import os
class TodoistService():
    def __init__(self) -> None:
        self.api = todoist.TodoistAPI(token=os.environ['TODOIST_TEST_ACCESS_TOKEN'], cache=".todoist-sync/")
    pass

    def sync(self):
        self.api.sync()
        print(f"Api state after sync: {self.api.state}")
