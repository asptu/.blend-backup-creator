#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

; Customise Hotkey here (https://www.autohotkey.com/docs/Hotkeys.htm)
^!b::

; Get Active Window Title
WinGetTitle, Title, A

; String Formatting
StringReplace, Title, Title, *, 
StringTrimLeft, Title, Title, 9
StringTrimRight, Title, Title, 7
StringReplace, TitleProc, Title, \, /, All

; Add formatted file path to .txt
FileDelete, path.txt
FileAppend, %TitleProc%, path.txt

; Runs Python copying script
Run, backup.py, , Min

return


