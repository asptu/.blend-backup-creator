
<img align="right" src="https://github.com/asptu/.blend-backup-creator/blob/main/readme_files/Blender_logo_no_text.svg.png" height="200" width="200">

# .blend backup creator

Creates .blend file backups via hotkey (made for my work)

### Requires
- [AutoHotkey](https://www.autohotkey.com/)
- [Python](https://www.python.org/)

### Running

Download the code above, chuck it in a folder and run [getwindow.ahk](https://github.com/asptu/.blend-backup-creator/blob/main/getwindow.ahk)

### Hotkey

Customise hotkey at the top of [getwindow.ahk](https://github.com/asptu/.blend-backup-creator/blob/main/getwindow.ahk)

```
; Default Hotkey (Ctrl + Alt + B)
^!b:: ; < Customise Hotkey here (see https://www.autohotkey.com/docs/Hotkeys.htm)
```

### Todo

- Compile into an executable to remove requirements
- Add functionality for programs other than Blender?
- Fix file numbering bug 