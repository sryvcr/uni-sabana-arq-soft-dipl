from abc import ABC, abstractmethod
from uuid import uuid4

from receiver import TaskManager


class ITaskCommand(ABC):
    id: str

    @abstractmethod
    def execute(self) -> None:
        pass


class CreateTaskCommand(ITaskCommand):
    def __init__(self, task: str, task_manager: TaskManager) -> None:
        self.id = str(uuid4())
        self._task = task
        self._task_manager = task_manager

    def execute(self) -> None:
        self._task_manager.create_task(task=self._task)


class EditTaskCommand(ITaskCommand):
    def __init__(self, task: str, task_manager: TaskManager) -> None:
        self.id = str(uuid4())
        self._task = task
        self._task_manager = task_manager

    def execute(self) -> None:
        self._task_manager.edit_task(task=self._task)


class DeleteTaskCommand(ITaskCommand):
    def __init__(self, task: str, task_manager: TaskManager) -> None:
        self.id = str(uuid4())
        self._task = task
        self.task_manager = task_manager

    def execute(self) -> None:
        self.task_manager.delete_task(task=self._task)


class CompleteTaskCommand(ITaskCommand):
    def __init__(self, task: str, task_manager: TaskManager) -> None:
        self.id = str(uuid4())
        self.task = task
        self._task_manager = task_manager

    def execute(self) -> None:
        self._task_manager.complete_task(task=self.task)
