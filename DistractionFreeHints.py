import sublime
import sublime_plugin
from typing import Optional, List
from . import distraction_free_hints_setting as SETTING
from . import settings_loader as SETTING_LOADER
import os
from threading import Timer

class DistractionFreeHintsCommand(sublime_plugin.TextCommand):

  print("distraction_free_hints command has loaded.")

  def run(self, edit: sublime.Edit) -> None:
    if self and self.view:
      self.log("distraction_free_hints is running")
      self.settings: SETTING.DistractionFreeHintsSetting = self.load_settings()
      self.debug(f'settings: {self.settings}')
      self.add_hints(self.view)
    else:
      sublime.message_dialog("Could not initialise plugin")


  def remove_hints(self, view: sublime.View):
    self.view.erase_regions("DistractionFreeHints")

  def add_hints(self, view: sublime.View):
    file_name = self.get_file_name(view)
    name = os.path.basename(file_name) if file_name else "untilted"
    self.show_annotation(view, name)
    t = Timer(5, self.remove_hints, [view])
    t.start()

  def show_annotation(self, view: sublime.View, file_name: str):
    self.remove_hints(view)

    cursor_pos: sublime.Region = view.sel()[0]
    self.debug(f"cursor: {cursor_pos}")

    header_markup = '''
        <body id="distraction-free-hints">
            <style>
                    .distraction-free-hints-file-name {{
                      background-color: gray;
                      color: white;
                    }}
            </style>
              <div class="distraction-free-hints-file-name">{}&nbsp;&nbsp;</div>
        </body>
    '''.format(file_name)

    view.add_regions(
      key = "DistractionFreeHints",
      regions = [view.sel()[0]],
      scope = '',
      icon = 'dot',
      flags = 0,
      annotations = [header_markup],
      annotation_color='darkseagreen',
      on_close = lambda: self.remove_hints(view)
    )

  def get_file_name(self, view: sublime.View) -> Optional[str]:
    file_name = self.view.file_name()
    if file_name:
      return file_name
    elif view.name():
      return view.name()
    else:
      return None


  def is_enabled(self) -> bool:
    return True

  def is_visible(self) -> bool:
    return True

  def load_settings(self) -> SETTING.DistractionFreeHintsSetting:
    loaded_settings: sublime.Settings = sublime.load_settings('DistractionFreeHints.sublime-settings')
    return SETTING_LOADER.SettingsLoader(loaded_settings).load()

  def log_with_context(self, message: str, context: Optional[str]):
    if context is not None:
      print(f'[DistractionFreeHints][{context}] - {message}')
    else:
      print(f'[DistractionFreeHints] - {message}')

  def log(self, message: str):
    self.log_with_context(message, context=None)

  def debug(self, message: str):
    if self.settings.debug:
      self.log_with_context(message, context="DEBUG")
