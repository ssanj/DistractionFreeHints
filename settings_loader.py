import sublime

from . import distraction_free_hints_setting as SETTING
from typing import TypeVar

class SettingsLoader:

  T = TypeVar('T')

  default_debug: bool = True
  default_foreground_color: str = "white"
  default_background_color: str = "gray"
  default_border_colour: str = "darkseagreen"
  default_auto_hide: bool = True
  default_auto_hide_duration: int = 5

  def __init__(self, settings: sublime.Settings) -> None:
    self.settings = settings

  def log(self, message: str):
    print(f'[DistractionFreeHints][WARN] - {message}')

  def load(self) -> SETTING.DistractionFreeHintsSetting:
    debug: bool = self.get_setting("debug", self.default_debug)
    foreground_colour: str = self.get_setting("foreground_colour", self.default_foreground_color)
    background_colour: str = self.get_setting("background_colour", self.default_background_color)
    border_colour: str = self.get_setting("border_colour", self.default_border_colour)
    auto_hide: bool = self.get_setting("auto_hide", self.default_auto_hide)
    auto_hide_duration: int = self.get_setting("auto_hide_duration", self.default_auto_hide_duration)

    return SETTING.DistractionFreeHintsSetting(debug, foreground_colour, background_colour, border_colour, auto_hide, auto_hide_duration)

  def get_setting(self, key: str, default_value: T) ->T:
    if self.settings.has(key):
      return self.settings.get(key)
    else:
      self.log(f'{key} setting not defined, defaulting to {str(default_value)}')
      return default_value

