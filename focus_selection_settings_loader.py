import sublime

from . import distraction_free_focus_selection_setting as SETTING
from typing import TypeVar

class SettingsLoader:

  T = TypeVar('T')

  default_debug: bool = True
  default_centre_edit: bool = True

  def __init__(self, settings: sublime.Settings) -> None:
    self.settings = settings

  def log(self, message: str):
    print(f'[DistractionFreeCentre][WARN] - {message}')

  def load(self) -> SETTING.DistractionFreeFocusSelectionSetting:
    debug: bool = self.get_setting("debug", self.default_debug)

    return SETTING.DistractionFreeFocusSelectionSetting(debug)

  def get_setting(self, key: str, default_value: T) ->T:
    if self.settings.has(key):
      return self.settings.get(key)
    else:
      self.log(f'{key} setting not defined, defaulting to {str(default_value)}')
      return default_value

