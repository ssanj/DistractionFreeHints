import sublime

from . import distraction_free_hints_setting as SETTING

class SettingsLoader:

  default_debug: bool = True

  def __init__(self, settings: sublime.Settings) -> None:
    self.settings = settings

  def log(self, message: str):
    print(f'[DistractionFreeHints][WARN] - {message}')

  def load(self) -> SETTING.DistractionFreeHintsSetting:
    debug: bool = self.get_debug()

    return SETTING.DistractionFreeHintsSetting(debug)

  def get_debug(self) -> bool:
    if self.settings.has("debug"):
      return self.settings.get("debug")
    else:
      self.log(f'debug setting not defined, defaulting to {SettingsLoader.default_debug}')
      return SettingsLoader.default_debug

