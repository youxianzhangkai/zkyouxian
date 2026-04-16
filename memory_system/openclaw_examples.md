# OpenClaw 内存系统使用示例

## 安装完成！

内存系统已经成功安装在：
`D:\openclaw-home\.openclaw\workspace\memory_system\`

你现在可以直接在OpenClaw中使用exec命令调用内存系统。

## 快速开始

### 1. 检查内存系统状态

```powershell
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' stats\""
```

### 2. 保存重要信息

```powershell
# 保存用户偏好
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'prohibited_phrases' '你说的对,你说的太对了,你说的正确,你说的完全正确,你说的太正确了' 'communication_rule'\""

# 保存项目信息
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'current_project' 'OpenClaw内存系统开发' 'project'\""
```

### 3. 读取记忆

```powershell
# 读取用户偏好
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' recall 'prohibited_phrases'\""
```

### 4. 搜索相关记忆

```powershell
# 搜索关于"工作流"的记忆
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' search '工作流'\""
```

## 完整使用示例

### 示例1：在对话中保存重要信息

```powershell
# 当用户提到重要信息时，保存到记忆系统
$important_info = "用户说：'我不喜欢那些客套话，直接说重点'"
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'user_communication_style' '$important_info' 'preference'\""
```

### 示例2：保存完整对话

```powershell
# 将当前对话保存到记忆系统
$session_id = "2026-04-15_内存系统安装"
$messages_json = '[{\"role\":\"user\",\"content\":\"你自己安装啊安装在D盘还要我自己动手呢\"},{\"role\":\"assistant\",\"content\":\"我理解你的意思。你希望我直接帮你安装这个内存系统插件...\"}]'
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' save '$session_id' '$messages_json'\""
```

### 示例3：在工作流中使用

```powershell
# 在稳健工作流中记录验证结果
$verification_result = "项目验证通过，所有检查项正常，时间：$(Get-Date)"
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'project_verification_001' '$verification_result' 'workflow'\""
```

## 高级用法

### 在Python脚本中集成

```python
# 创建Python脚本 memory_integration.py
import subprocess
import json

def save_to_memory(key, value, category="general"):
    """保存信息到内存系统"""
    cmd = f"powershell -Command \"& 'D:\\openclaw-home\\.openclaw\\workspace\\memory_system\\memory_simple.ps1' remember '{key}' '{value}' '{category}'\""
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return json.loads(result.stdout)

def recall_from_memory(key):
    """从内存系统读取信息"""
    cmd = f"powershell -Command \"& 'D:\\openclaw-home\\.openclaw\\workspace\\memory_system\\memory_simple.ps1' recall '{key}'\""
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return json.loads(result.stdout).get('value')

# 使用示例
save_to_memory("project_status", "开发完成，等待测试", "project")
memory_value = recall_from_memory("project_status")
print(f"项目状态: {memory_value}")
```

### 创建自动化任务

```powershell
# 创建定时备份脚本 memory_backup.ps1
$backup_time = Get-Date -Format "yyyy-MM-dd_HHmm"
$backup_file = "D:\openclaw-home\.openclaw\workspace\memory\backup_$backup_time.db"

# 备份数据库
Copy-Item "D:\openclaw-home\.openclaw\workspace\memory\conversations.db" $backup_file

# 记录备份信息
$backup_info = "数据库备份完成，文件：$backup_file，大小：$(Get-Item $backup_file).Length bytes"
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' remember 'db_backup_$backup_time' '$backup_info' 'system'\""
```

## 实用命令参考

### 基本命令

| 命令 | 说明 | 示例 |
|------|------|------|
| `stats` | 获取统计信息 | `exec "powershell ... stats"` |
| `save` | 保存对话 | `exec "powershell ... save 'session_id' 'messages_json'"` |
| `load` | 加载对话 | `exec "powershell ... load 'session_id'"` |
| `search` | 搜索记忆 | `exec "powershell ... search '关键词'"` |
| `remember` | 保存记忆 | `exec "powershell ... remember 'key' 'value'"` |
| `recall` | 读取记忆 | `exec "powershell ... recall 'key'"` |
| `list` | 列出会话 | `exec "powershell ... list"` |

### 常用场景命令

1. **记录用户偏好**
   ```powershell
   exec "powershell -Command \"& '...\memory_simple.ps1' remember 'user_likes_direct' 'true' 'preference'\""
   ```

2. **保存项目进度**
   ```powershell
   exec "powershell -Command \"& '...\memory_simple.ps1' remember 'project_memory_system' '开发完成，测试通过' 'project_status'\""
   ```

3. **搜索历史决策**
   ```powershell
   exec "powershell -Command \"& '...\memory_simple.ps1' search '决策'\""
   ```

4. **备份重要对话**
   ```powershell
   $session_data = '[{\"role\":\"user\",\"content\":\"重要内容\"}]'
   exec "powershell -Command \"& '...\memory_simple.ps1' save 'important_$(Get-Date -Format 'yyyyMMdd')' '$session_data'\""
   ```

## 故障排除

### 常见问题

1. **命令执行失败**
   ```
   错误: 系统找不到指定的路径
   ```
   解决方案：确保路径正确，特别是反斜杠需要转义

2. **JSON格式错误**
   ```
   错误: 无效的JSON格式
   ```
   解决方案：确保JSON字符串正确转义，使用`\"`而不是`"`

3. **Python未找到**
   ```
   'python' 不是内部或外部命令
   ```
   解决方案：确保Python已安装并添加到PATH，或使用完整路径

### 测试命令

```powershell
# 测试Python环境
exec "python --version"

# 测试内存系统基础功能
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory_simple.ps1' stats\""

# 运行完整测试
exec "cd D:\openclaw-home\.openclaw\workspace\memory_system && test_simple.bat"
```

## 数据管理

### 数据库位置
- 主数据库：`D:\openclaw-home\.openclaw\workspace\memory\conversations.db`
- 备份目录：`D:\openclaw-home\.openclaw\workspace\memory\backup\`

### 查看数据库内容
```powershell
# 使用SQLite查看工具
exec "sqlite3 D:\openclaw-home\.openclaw\workspace\memory\conversations.db \"SELECT * FROM memories LIMIT 5;\""
```

### 备份数据库
```powershell
# 手动备份
exec "Copy-Item D:\openclaw-home\.openclaw\workspace\memory\conversations.db D:\openclaw-home\.openclaw\workspace\memory\backup\conversations_$(Get-Date -Format 'yyyyMMdd_HHmmss').db"
```

## 扩展功能

### 添加自定义命令

1. 在 `memory_core.py` 中添加新方法
2. 在 `memory_cli.py` 中添加命令行接口
3. 在 `memory_simple.ps1` 中添加PowerShell包装

### 集成到其他系统

```python
# 与其他Python工具集成
import sys
sys.path.append("D:\\openclaw-home\\.openclaw\\workspace\\memory_system")
from memory_core import MemorySystem

memory = MemorySystem()
# 直接使用内存系统API
```

## 总结

内存系统已经成功安装并可以使用。主要特点：

1. ✅ **无需复杂安装**：直接通过exec命令调用
2. ✅ **功能完整**：支持保存、加载、搜索、记忆管理
3. ✅ **数据安全**：SQLite数据库，本地存储
4. ✅ **易于使用**：简单的PowerShell命令接口
5. ✅ **与OpenClaw完美集成**：原生exec命令支持

现在你可以直接在OpenClaw中使用这个内存系统来：
- 保存重要对话和决策
- 记录用户偏好和习惯
- 搜索历史信息和经验
- 管理项目状态和进度

**安装完成！内存系统已就绪，可以开始使用了。**