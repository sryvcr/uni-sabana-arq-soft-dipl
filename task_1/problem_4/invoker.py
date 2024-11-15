from command import ITaskCommand


class ActionManager:
    def __init__(self) -> None:
        self._history = {}

    def execute_action(self, command: ITaskCommand) -> None:
        command.execute()
        self._history[command.id] = command

    def revert_action(self, command_id: str) -> None:
        self._revert_command(command_id=command_id)
        del self._history[command_id]

    def _revert_command(self, command_id: str) -> None:
        print(f"command_id {command_id} reverted")
