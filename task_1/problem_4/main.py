from invoker import ActionManager
from receiver import TaskManager
from command import (
    CreateTaskCommand, CompleteTaskCommand, EditTaskCommand,
)


def main():
    task_manager = TaskManager()
    action_manager = ActionManager()

    task_1 = "Task 1"
    task_2 = "Task 2"

    cmd1 = CreateTaskCommand(task_1, task_manager)
    cmd2 = CompleteTaskCommand(task_1, task_manager)
    cmd3 = CreateTaskCommand(task_2, task_manager)
    cmd4 = EditTaskCommand(task_2, task_manager)

    action_manager.execute_action(command=cmd1)
    action_manager.execute_action(command=cmd2)
    action_manager.execute_action(command=cmd3)
    action_manager.execute_action(command=cmd4)

    action_manager.revert_action(command_id=cmd2.id)
    action_manager.revert_action(command_id=cmd4.id)


if __name__ == "__main__":
    main()
