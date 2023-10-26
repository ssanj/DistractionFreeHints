import sublime
import sublime_plugin
from . import distraction_free_centre_setting as SETTING
from . import centre_settings_loader as SETTING_LOADER
from typing import Optional, List


class DistractionFreeCentreCommand(sublime_plugin.EventListener):

  print("DistractionFreeCentre loaded")

  def __init__(self) -> None:
    super().__init__()

  def on_load_async(self, view: sublime.View):
    print(f"DistractionFreeCentre: Loaded {view}")
    self.settings: SETTING.DistractionFreeCentreSetting = self.load_settings()
    self.debug(f'settings: {self.settings}')

  def on_modified_async(self, view: sublime.View):
    # Sometimes this function is called before on_load_async
    if hasattr(self, "settings") and self.settings.centre_edit:
      # Sometimes the view selection has not been set either
      if view.sel():
        r = view.sel()[0]
        view.show_at_center(r)

  def load_settings(self) -> SETTING.DistractionFreeCentreSetting:
    loaded_settings: sublime.Settings = sublime.load_settings('DistractionFreeHints.sublime-settings')
    return SETTING_LOADER.SettingsLoader(loaded_settings).load()

  def log_with_context(self, message: str, context: Optional[str]):
    if context is not None:
      print(f'[DistractionFreeCentre][{context}] - {message}')
    else:
      print(f'[DistractionFreeCentre] - {message}')

  def log(self, message: str):
    self.log_with_context(message, context=None)

  def debug(self, message: str):
    if self.settings.debug:
      self.log_with_context(message, context="DEBUG")
