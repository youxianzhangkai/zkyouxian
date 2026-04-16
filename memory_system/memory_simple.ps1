# OpenClaw 内存系统简单PowerShell脚本

param(
    [string]$Command,
    [string]$Arg1,
    [string]$Arg2,
    [string]$Arg3,
    [string]$Arg4
)

# 设置路径
$workspace = "D:\openclaw-home\.openclaw\workspace"
$pythonScript = "$workspace\memory_system\memory_cli.py"

# 检查Python脚本
if (-not (Test-Path $pythonScript)) {
    Write-Output "错误: 找不到脚本 $pythonScript"
    exit 1
}

# 构建命令
if ($Command -eq "stats") {
    python $pythonScript stats
}
elseif ($Command -eq "save") {
    if (-not $Arg1 -or -not $Arg2) {
        Write-Output "错误: save需要session_id和messages_json"
        exit 1
    }
    python $pythonScript save $Arg1 $Arg2
}
elseif ($Command -eq "load") {
    if (-not $Arg1) {
        Write-Output "错误: load需要session_id"
        exit 1
    }
    if ($Arg2) {
        python $pythonScript load $Arg1 $Arg2
    } else {
        python $pythonScript load $Arg1
    }
}
elseif ($Command -eq "search") {
    if (-not $Arg1) {
        Write-Output "错误: search需要query"
        exit 1
    }
    if ($Arg2) {
        python $pythonScript search $Arg1 $Arg2
    } else {
        python $pythonScript search $Arg1
    }
}
elseif ($Command -eq "remember") {
    if (-not $Arg1 -or -not $Arg2) {
        Write-Output "错误: remember需要key和value"
        exit 1
    }
    if ($Arg3) {
        python $pythonScript remember $Arg1 $Arg2 $Arg3
    } else {
        python $pythonScript remember $Arg1 $Arg2
    }
}
elseif ($Command -eq "recall") {
    if (-not $Arg1) {
        Write-Output "错误: recall需要key"
        exit 1
    }
    python $pythonScript recall $Arg1
}
elseif ($Command -eq "list") {
    if ($Arg1) {
        python $pythonScript list $Arg1
    } else {
        python $pythonScript list
    }
}
elseif ($Command -eq "help") {
    Write-Output "OpenClaw 内存系统命令:"
    Write-Output "  stats - 获取统计信息"
    Write-Output "  save <session_id> <messages_json> - 保存对话"
    Write-Output "  load <session_id> [limit] - 加载对话"
    Write-Output "  search <query> [limit] - 搜索记忆"
    Write-Output "  remember <key> <value> [category] - 保存记忆"
    Write-Output "  recall <key> - 回忆记忆"
    Write-Output "  list [limit] - 列出会话"
}
else {
    Write-Output "未知命令: $Command"
    Write-Output "使用 'memory_simple.ps1 help' 查看帮助"
}