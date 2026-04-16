# OpenClaw 内存系统 - 快速开始指南

## 🎯 安装完成！

内存系统已经成功安装在你的D盘：
`D:\openclaw-home\.openclaw\workspace\memory_system\`

**无需任何额外配置**，你现在可以直接在OpenClaw中使用。

## 🚀 立即使用

### 基本命令格式

```powershell
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' <命令> <参数>\""
```

### 常用命令示例

#### 1. 检查系统状态
```powershell
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' stats\""
```

#### 2. 保存重要信息
```powershell
# 保存用户偏好
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'user_preference' '喜欢直接简洁的回答' 'communication'\""

# 保存项目状态
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'project_status' '内存系统安装完成' 'project'\""
```

#### 3. 读取记忆
```powershell
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' recall 'user_preference'\""
```

#### 4. 搜索相关记忆
```powershell
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' search '内存'\""
```

## 📝 实际应用场景

### 场景1：记录对话中的重要信息

当用户提到重要信息时，立即保存：

```powershell
# 用户说："我不喜欢客套话"
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'user_dislikes' '不喜欢客套话，喜欢直接说重点' 'preference'\""
```

### 场景2：保存完整对话

将重要对话保存下来，便于后续回顾：

```powershell
$session_id = "重要对话_$(Get-Date -Format 'yyyyMMdd_HHmm')"
$messages = '[{\"role\":\"user\",\"content\":\"重要内容\"},{\"role\":\"assistant\",\"content\":\"我的回答\"}]'
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' save '$session_id' '$messages'\""
```

### 场景3：在工作流中记录验证结果

在稳健工作流或磐石工作流中使用：

```powershell
# 记录验证开始
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'verification_start' '开始验证项目，时间：$(Get-Date)' 'workflow'\""

# ... 执行验证 ...

# 记录验证结果
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'verification_result' '验证通过，所有检查正常' 'workflow'\""
```

## 🔧 命令参考表

| 命令 | 说明 | 示例 |
|------|------|------|
| `stats` | 系统统计 | `exec "powershell ... stats"` |
| `save` | 保存对话 | `exec "powershell ... save 'session_id' 'json_messages'"` |
| `load` | 加载对话 | `exec "powershell ... load 'session_id'"` |
| `search` | 搜索记忆 | `exec "powershell ... search '关键词'"` |
| `remember` | 保存记忆 | `exec "powershell ... remember 'key' 'value'"` |
| `recall` | 读取记忆 | `exec "powershell ... recall 'key'"` |
| `list` | 列出会话 | `exec "powershell ... list"` |

## 🎨 个性化配置

### 记录你的偏好

```powershell
# 1. 沟通风格偏好
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'communication_style' '直接、简洁、务实' 'preference'\""

# 2. 工作习惯
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'work_habit' '喜欢系统化、有文档、可追溯' 'preference'\""

# 3. 技术偏好
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'tech_preference' 'Python、PowerShell、SQLite' 'preference'\""
```

### 创建项目记忆

```powershell
# 当前项目状态
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'current_project' 'OpenClaw内存系统开发' 'project'\""

# 项目目标
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'project_goal' '创建无需插件的内存系统，直接通过exec调用' 'project'\""

# 项目进度
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'project_progress' '已完成：核心功能、命令行接口、PowerShell包装、测试脚本' 'project'\""
```

## 🧪 测试你的安装

运行完整测试：

```powershell
# 方法1：运行测试脚本
exec "cd D:\openclaw-home\.openclaw\workspace\memory_system && test_simple.bat"

# 方法2：手动测试
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' stats\""
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'test' '测试记忆' 'test'\""
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' recall 'test'\""
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' search '测试'\""
```

## 📊 查看系统状态

### 数据库信息
- 位置：`D:\openclaw-home\.openclaw\workspace\memory\conversations.db`
- 查看：`exec "sqlite3 D:\openclaw-home\.openclaw\workspace\memory\conversations.db \".tables\""`

### 统计信息
```powershell
# 获取详细统计
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' stats\""
```

## 🔄 数据备份

### 手动备份
```powershell
exec "Copy-Item D:\openclaw-home\.openclaw\workspace\memory\conversations.db D:\openclaw-home\.openclaw\workspace\memory\backup\conversations_$(Get-Date -Format 'yyyyMMdd').db"
```

### 自动备份（通过cron）
```powershell
# 创建每日备份任务
# （需要配置OpenClaw cron）
```

## 🚨 故障排除

### 问题1：命令执行失败
**症状**：`'python' 不是内部或外部命令`
**解决**：确保Python已安装，或使用完整路径

### 问题2：JSON格式错误
**症状**：`错误: 无效的JSON格式`
**解决**：确保JSON字符串正确转义，使用`\"`而不是`"`

### 问题3：文件路径错误
**症状**：`错误: 找不到脚本`
**解决**：检查路径是否正确：`D:\openclaw-home\.openclaw\workspace\memory_system\`

### 快速诊断
```powershell
# 检查Python
exec "python --version"

# 检查脚本路径
exec "Test-Path D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1"

# 测试基本功能
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' stats\""
```

## 📈 高级用法

### 在Python脚本中集成
```python
import subprocess
import json

def memory_command(cmd, *args):
    """调用内存系统命令"""
    script = r"D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1"
    cmd_args = ["powershell", "-Command", f"& '{script}' {cmd}"]
    cmd_args.extend(args)
    
    result = subprocess.run(cmd_args, capture_output=True, text=True)
    return json.loads(result.stdout)

# 使用示例
stats = memory_command("stats")
print(f"会话数量: {stats.get('session_count', 0)}")
```

### 创建自动化工作流
```powershell
# 工作流开始：记录
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'workflow_start' '开始稳健工作流，项目：XXX' 'workflow'\""

# 工作流执行：记录每个阶段
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'stage_1_complete' '阶段1：需求分析完成' 'workflow'\""

# 工作流结束：总结
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'workflow_complete' '工作流完成，结果：成功' 'workflow'\""
```

## 🎉 恭喜！

你的OpenClaw内存系统已经**完全安装并可以使用**！

### 已安装的功能：
1. ✅ **内存核心系统** - 完整的SQLite数据库管理
2. ✅ **命令行接口** - Python和PowerShell两种方式
3. ✅ **OpenClaw集成** - 直接通过exec命令调用
4. ✅ **测试套件** - 完整的测试脚本
5. ✅ **使用文档** - 详细的指南和示例

### 立即尝试：
```powershell
# 试试这个命令，查看系统状态
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' stats\""
```

**内存系统已就绪，开始记录你的重要信息和对话吧！**