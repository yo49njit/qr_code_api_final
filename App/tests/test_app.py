import builtins
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import App
from App.plugins.add import Add
import pytest



def test_app_command_execution(monkeypatch, capsys):
    inputs = iter(['add', '2', '3', 'exit'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))

    app = App.App()
    app.command_handler.register_command("exit", lambda: exit())

    with pytest.raises(SystemExit):
        app.start()

    captured = capsys.readouterr()
    assert "2.0 + 3.0 = 5.0" in captured.out
