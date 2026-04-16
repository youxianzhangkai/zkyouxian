<![CDATA[# OpenClaw 内存系统 PowerShell 包装脚本
# 通过exec命令调用Python内存系统

param(
    [string]$Command,
    [string]$Arg1,
    [string]$Arg2,
    [string]$Arg3,
    [string]$Arg4
)

# 设置工作目录
$workspace = "D:\openclaw-home\.openclaw\workspace"
$pythonScript = "$workspace\memory_system\memory_cli.py"

# 检查Python脚本是否存在
if (-not (Test-Path $pythonScript)) {
    Write-Output "错误: 找不到内存系统脚本 $pythonScript"
    exit 1
}

# 构建Python命令
$pythonArgs = @()

switch ($Command.ToLower()) {
    "save" {
        if (-not $Arg1 -or -not $Arg2) {
            Write-Output "错误: save命令需要session_id和messages_json参数"
            exit 1
        }
        $pythonArgs = @("save", $Arg1, $Arg2)
    }
    "load" {
        if (-not $Arg1) {
            Write-Output "错误: load命令需要session_id参数"
            exit 1
        }
        $pythonArgs = @("load", $Arg1)
        if ($Arg2) { $pythonArgs += $Arg2 }
    }
    "search" {
        if (-not $Arg1) {
            Write-Output "错误: search命令需要query参数"
            exit 1
        }
        $pythonArgs = @("search", $Arg1)
        if ($Arg2) { $pythonArgs += $Arg2 }
    }
    "remember" {
        if (-not $Arg1 -or -not $Arg2) {
            Write-Output "错误: remember命令需要key和value参数"
            exit 1
        }
        $pythonArgs = @("remember", $Arg1, $Arg2)
        if ($Arg3) { $pythonArgs += $Arg3 }
    }
    "recall" {
        if (-not $Arg1) {
            Write-Output "错误: recall命令需要key参数"
            exit 1
        }
        $pythonArgs = @("recall", $Arg1)
    }
    "stats" {
        $pythonArgs = @("stats")
    }
    "list" {
        $pythonArgs = @("list")
        if ($Arg1) { $pythonArgs += $Arg1 }
    }
    "help" {
        Write-Output "OpenClaw 内存系统命令:"
        Write-Output "  save <session_id> <messages_json> - 保存对话"
        Write-Output "  load <session_id> [limit] - 加载对话"
        Write-Output "  search <query> [limit] - 搜索记忆"
        Write-Output "  remember <key> <value> [category] - 保存记忆"
        Write-Output "  recall <key> - 回忆记忆"
        Write-Output "  stats - 获取统计信息"
        Write-Output "  list [limit] - 列出会话"
        exit 0
    }
    default {
        Write-Output "未知命令: $Command"
        Write-Output "使用 'memory.ps1 help' 查看帮助"
        exit 1
    }
}

# 执行Python命令
try {
    $output = python $pythonScript $pythonArgs 2>&1
    Write-Output $output
} catch {
    Write-Output "执行错误: $_"
    exit 1
}