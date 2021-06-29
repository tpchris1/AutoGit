@echo off

title 每日报告一键提交

echo 正在暂存有更新的文件...
echo.
git add .
echo.

set declation=新增今日报告
set /p declation=请输入提交的commit信息（直接回车则为显示“新增今日报告”）:
git commit -m "%declation%"
echo.
@REM git commit -m "新增今日报告"

echo 正在上传文件到Gitlab...
echo.
git push
echo.

echo 所有文件已经上传到Gitlab
echo.

pause