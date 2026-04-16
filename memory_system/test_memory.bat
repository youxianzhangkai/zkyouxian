@echo off
REM OpenClaw 内存系统测试脚本

echo 测试OpenClaw内存系统...
echo.

REM 测试1: 获取统计信息
echo 1. 获取统计信息:
powershell -Command "& '%~dp0memory.ps1' stats"
echo.

REM 测试2: 保存记忆
echo 2. 保存测试记忆:
powershell -Command "& '%~dp0memory.ps1' remember 'test_key' '这是一个测试记忆' 'test'"
echo.

REM 测试3: 回忆记忆
echo 3. 回忆测试记忆:
powershell -Command "& '%~dp0memory.ps1' recall 'test_key'"
echo.

REM 测试4: 搜索记忆
echo 4. 搜索记忆:
powershell -Command "& '%~dp0memory.ps1' search '测试'"
echo.

REM 测试5: 列出会话
echo 5. 列出会话:
powershell -Command "& '%~dp0memory.ps1' list"
echo.

echo 测试完成!
pause