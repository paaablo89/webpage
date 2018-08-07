@echo off

set /p commitMessage= Commit message:
echo.

echo Commiting 'Webpage'

echo.
git add -A

git commit -m "Laptop: %commitMessage%"

git push origin master

echo.
pause