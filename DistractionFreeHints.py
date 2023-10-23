import sublime
import sublime_plugin
from typing import Optional, List
from . import distraction_free_hints_setting as SETTING
from . import settings_loader as SETTING_LOADER
import os

class DistractionFreeHintsCommand(sublime_plugin.TextCommand):

  print("distraction_free_hints command has loaded.")

  def run(self, edit: sublime.Edit, **args) -> None:
    if self and self.view:
      self.log("distraction_free_hints is running")
      self.settings: SETTING.DistractionFreeHintsSetting = self.load_settings()
      self.debug(f'settings: {self.settings}')
      self.debug(f'args: {args}')

      reset: bool = True if args.get("reset") == True else False

      if self.view:
        if reset:
          self.remove_hints(self.view)
        else:
          self.add_hints(self.view)

    else:
      sublime.message_dialog("Could not initialise plugin")


  def remove_hints(self, view: sublime.View):
    self.view.erase_phantoms("DistractionFreeHints") # remove all existing phantoms
    self.ps = sublime.PhantomSet(view, "DistractionFreeHints")
    self.phantoms: list[sublime.Phantom] = []

  def add_hints(self, view: sublime.View):
    file_name = self.get_file_name(view)
    name = os.path.basename(file_name)
    self.show_phantom(view, name)

  def show_phantom(self, view: sublime.View, file_name: str):
    self.view.erase_phantoms("DistractionFreeHints") # remove all existing phantoms
    self.ps = sublime.PhantomSet(view, "DistractionFreeHints")
    self.phantoms = []

    cursor_pos: sublime.Region = view.sel()[0]
    self.debug(f"cursor: {cursor_pos}")

    header_markup = '''
        <body id="distraction-free-hints">
            <style>
                    .distraction-free-hints-file-name {{
                      background-color: gray;
                      padding: 5px;
                      color: white;
                      font-weight: bold;
                      margin: 20px;
                    }}

            </style>
            <H3 class="distraction-free-hints-file-name">{}</H3>
        </body>
    '''.format(file_name)

    self.phantoms.append(sublime.Phantom(cursor_pos, header_markup, sublime.LAYOUT_BLOCK, on_navigate=lambda href: self.remove_hints(view)));
    self.ps.update(self.phantoms)

  def get_file_name(self, view: sublime.View):
    file_name = self.view.file_name()
    if file_name:
      return file_name
    else:
      return "<Untitled>"


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
