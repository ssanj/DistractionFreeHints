class DistractionFreeHintsSetting:
  def __init__(self, debug: bool, foreground_colour: str, background_colour: str, border_colour: str, auto_hide: bool, auto_hide_duration: int) -> None:
    self.debug = debug
    self.foreground_colour = foreground_colour
    self.background_colour = background_colour
    self.border_colour = border_colour
    self.auto_hide = auto_hide
    self.auto_hide_duration = auto_hide_duration

  def __str__(self) -> str:
    return f"DistractionFreeHintsSetting(debug={self.debug}, foreground_colour={self.foreground_colour}, background_colour={self.background_colour}, border_colour={self.border_colour}, auto_hide={self.auto_hide}, auto_hide_duration={self.auto_hide_duration})"

  def __repr__(self) -> str:
    return self.__str__()
