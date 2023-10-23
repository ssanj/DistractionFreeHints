import unittest

import distraction_free_hints_setting as S

# Example test with valid imports and a test to get started.
class SettingTest(unittest.TestCase):

  def test_str(self):
    settings = S.DistractionFreeHintsSetting(debug = True)
    self.assertEqual("DistractionFreeHintsSetting(debug=True)", str(settings))
