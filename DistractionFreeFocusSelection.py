import sublime
import sublime_plugin
from typing import Optional
from . import distraction_free_focus_selection_setting as SETTING
from . import focus_selection_settings_loader as SETTING_LOADER
import os

class DistractionFreeFocusSelectionCommand(sublime_plugin.TextCommand):

  print("distraction_free_focus_selection command has loaded.")

  def run(self, edit: sublime.Edit) -> None:
    if self and self.view:
      self.log("distraction_free_focus_selection is running")
      self.settings: SETTING.DistractionFreeFocusSelectionSetting = self.load_settings()
      self.debug(f'settings: {self.settings}')
      if hasattr(self, "folded"):
        if not self.folded:
          self.debug("not folded")
          self.focus_selection(edit, self.view)
        else:
          self.debug("already folded")
          self.view.run_command('unfold_all')
          self.folded = False
          if hasattr(self, "ps"):
            self.ps.update([])

          self.view.show_at_center(self.view.sel()[0])
      else:
        self.debug("no attribute")
        self.focus_selection(edit, self.view)
    else:
      sublime.message_dialog("Could not initialise plugin")

  def focus_selection(self, edit:sublime.Edit, view: sublime.View):
    selection = view.sel();
    if len(selection) > 0 and selection[0].begin() != selection[0].end(): # we need at least one
      self.ps = sublime.PhantomSet(view, "focus_selection")
      # Find the line above the selection
      top_line = max(self.region_to_row(view, selection[0]) - 1, 0)

      # Find its region
      top_region = self.row_to_region(view, top_line)
      # Expand the selection to include the line above the initial selection
      # We want to do this so that the focus block is displayed "above" the selection
      # and not "within" it.
      view.sel().add(top_region)

      focus_block = '''<body id="focus-block">
                <style>
                        .focus-block {
                          color: gray;
                          font-weight: bold;
                          margin-top: 100px;
                          margin-bottom: 20px;
                        }
                </style>
                <H1 class="focus-block">Focus Block</H1>
            </body>'''
      phantoms = [
          sublime.Phantom(top_region, focus_block, sublime.LAYOUT_INLINE)
        ]
      self.ps.update(phantoms)
      # Select everything but the selection
      view.run_command('invert_selection')
      # Fold everything selected in the above
      sublime.set_timeout(lambda: self.fold_selection(view, selection), 10)
    else:
      sublime.message_dialog("There needs to be a selection to focus on")

  def fold_selection(self, view: sublime.View, selection: sublime.Selection):
      new_selection = view.sel()
      for s in new_selection:
        view.fold(s)

      self.folded = True

      # Clear the inverted selection so it doesn't show multiple cursors for areas above and below the initial selection.
      view.sel().clear()


  def region_to_row(self, view: sublime.View, region: sublime.Region) -> int:
    start = region.begin()
    (row, _) = view.rowcol(start)
    return row + 1

  def row_to_region(self, view: sublime.View, row: int) -> sublime.Region:
    # row should be zero-based to text_point, but we use 1-base in the code
    point = view.text_point(max(row - 1, 0), 0)
    return view.line(point)

  def load_settings(self) -> SETTING.DistractionFreeFocusSelectionSetting:
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
