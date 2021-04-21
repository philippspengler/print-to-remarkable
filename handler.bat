set LOGFILE=%~dp0\batch.log
call :LOG > %LOGFILE%
exit /B

:LOG

set datestr=%date%
set result=%datestr:/=-%

"%PROGRAMFILES%\gs\gs9.54.0\bin\gswin64c.exe" -dBATCH -dSAFER -dNOPAUSE -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -dAutoRotatePages=/PageByPage -r600 -sOutputFile="%~dp0%result%.pdf" -
^&
"%~dp0upload.py" "%result%.pdf"
