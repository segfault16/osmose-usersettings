# osmose-usersettings

User preset bank for Expressive E Osmose and tooling for reordering/renaming user presets

## Usage

The [state](state) folder contains the current snapshot from Osmose.
To transfer your own user settings dump them with Osmose Updater in Advanced Mode and place all files in [state](state) folder.

Run `task deconstruct` with [Taskfile.dev tooling](https://taskfile.dev) to generate a state.txt from state/group*.txt without the line information.

Modify [state.txt](state.txt) to re-order presets.

Once you're happy run `task construct` to generate new state/group*.txt files from [state.txt](state.txt).

To rename presets use `task rename SRC="another big one pad" TRG="whatever you want"` to rename the preset midi file and update [state.txt](state.txt) as well as the group files.

Again use Osmose Updater in Advanced Mode to restore [state](state) folder to user presets in Osmose.