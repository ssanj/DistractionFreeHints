# DistractionFreeHints

[Sublime Text](https://www.sublimetext.com/) plugin that shows hints when in `Distraction Free` mode.

![]()

## Installation

- Open the command palette with `CMD + SHIFT + P`
- Select `Package Control: Add Repository`
- Enter https://github.com/ssanj/DistractionFreeHints for the repository
- Select `Package Control: Install Package`
- Choose DistractionFreeHints


## Functionality

One issue with `Distraction Free` mode in Sublime Text, is that it doesn't have a way to show the name of the current file
you're working on. This can be disorienting when you are working across multiple files in full screen but haven no idea
which one it is.

`DistractionFreeHints` provides a command to display the current file name. It automatically hides the hint after a given
time so as not to distract from your workflow. These settings are customisable.

You can run it by pressing `CMD` + `SHIFT` + `P`
to open the command pallet and choosing `DistractionFreeHints: Add Filename`.

![Distraction-Free Hints](distraction-free-hints.png)

You can also assign a shortcut key to it. Choose `Preferences: Key Bindings` through the command palette and add
in the following entry:

```json
{ "keys": ["YOUR_KEY_COMBOS"], "command": "distraction_free_hints" }
```

## Settings

The following settings are supported:

```
{
  // Whether to turn on debug logging
  "debug": true

  // See https://www.sublimetext.com/docs/color_schemes.html for available colours.
  // hint text colour
  "foreground_colour": "gray",

  // hint background colour
  "background_colour": "white",

  // border colour
  // "border_colour": "darkseagreen",

  // autohide hint
  // Whether to hide the hint automatically after a duration of 'auto_hide_duration'.
  // If this is false, you will need to close the hint yourself by clicking the 'x' next to it.
  "auto_hide": true,

  // autohide duration in seconds
  // If 'auto_hide' is set to 'true', the hint is automatically hidden after this duration.
  "auto_hide_duration": 5,
}

```
