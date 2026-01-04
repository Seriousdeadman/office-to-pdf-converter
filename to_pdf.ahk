#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


^²::
    Run, "C:\Users\abdel\AppData\Local\Programs\Python\Python313\python.exe" "C:\Users\abdel\PycharmProjects\to_pdf\main.py"
return