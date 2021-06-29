@echo off

title 每日报告一键拉取

echo 正在从Gitlab同步...
echo.

git pull
echo.

echo 从Gitlab同步完成！
echo.
echo 正在啟動Visual Studion Code...

code .