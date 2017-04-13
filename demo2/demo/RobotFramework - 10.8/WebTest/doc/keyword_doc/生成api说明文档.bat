@echo off&setlocal
for /f "tokens=*" %%a in ('findstr /s /m Keywords  ../../*.txt') do (
	 python C:\Python27\Lib\site-packages\robot\libdoc.py -f html  "%%~dpnxa"  "%%~na.html"
)
pause