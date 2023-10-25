class DistractionFreeCentreSetting:
  def __init__(self, debug: bool, centre_edit: bool) -> None:
    self.debug = debug
    self.centre_edit = centre_edit

  def __str__(self) -> str:
    return f"DistractionFreeCentreSetting(debug={self.debug}, centre_edit={self.centre_edit})"

  def __repr__(self) -> str:
    return self.__str__()
