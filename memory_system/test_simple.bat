@echo off
echo OpenClaw 内存系统测试
echo.

echo 1. 测试统计信息:
powershell -Command "& '%~dp0memory_simple.ps1' stats"
echo.

echo 2. 测试保存记忆:
powershell -Command "& '%~dp0memory_simple.ps1' remember 'user_name' '张凯' 'user_info'"
echo.

echo 3. 测试读取记忆:
powershell -Command "& '%~dp0memory_simple.ps1' recall 'user_name'"
echo.

echo 4. 测试搜索记忆:
powershell -Command "& '%~dp0memory_simple.ps1' search '张凯'"
echo.

echo 5. 测试保存对话:
set messages=[{\"role\":\"user\",\"content\":\"你好\"},{\"role\":\"assistant\",\"content\":\"你好！我是守拙\"}]
powershell -Command "& '%~dp0memory_simple.ps1' save 'test_session_001' '%messages%'"
echo.

echo 6. 测试加载对话:
powershell -Command "& '%~dp0memory_simple.ps1' load 'test_session_001'"
echo.

echo 测试完成！
pause