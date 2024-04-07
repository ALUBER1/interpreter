if not exist "c:\MinGW" (
	move "MinGW" c:\
	md MinGW
	xcopy /s /e /i c:\MinGW MinGW
	cd interpretatore
exit
)