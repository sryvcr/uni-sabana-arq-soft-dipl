class TaskManager:
    def create_task(self, task: str) -> None:
        print(f"task {task} added")

    def edit_task(self, task: str) -> None:
        print(f"task {task} edited")

    def delete_task(self, task: str) -> None:
        print(f"task {task} deleted")

    def complete_task(self, task: str) -> None:
        print(f"task {task} completed")
