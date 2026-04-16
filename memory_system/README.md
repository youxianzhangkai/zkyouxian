# OpenClaw 内存系统

一个简单但完整的内存管理系统，专为OpenClaw设计，可以通过exec命令直接调用。

## 特点

- ✅ **无需插件安装**：直接通过exec命令调用
- ✅ **完整功能**：对话保存、记忆管理、搜索功能
- ✅ **简单易用**：PowerShell和Python两种调用方式
- ✅ **数据安全**：使用SQLite数据库，数据持久化
- ✅ **与OpenClaw原生集成**：完美配合OpenClaw的exec工具

## 文件结构

```
memory_system/
├── memory_core.py      # 内存系统核心模块
├── memory_cli.py       # Python命令行接口
├── memory.ps1          # PowerShell包装脚本
├── openclaw_integration.py  # OpenClaw集成模块
├── test_memory.bat     # 测试脚本
└── README.md           # 说明文档
```

## 安装

无需安装！文件已经放在正确的位置：
`D:\openclaw-home\.openclaw\workspace\memory_system\`

## 使用方法

### 方法1：通过OpenClaw exec命令直接调用

```powershell
# 获取统计信息
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory.ps1' stats\""

# 保存记忆
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory.ps1' remember 'user_preference' '喜欢简洁的回答' 'preference'\""

# 搜索记忆
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory.ps1' search '喜欢'\""
```

### 方法2：在Python脚本中调用

```python
import sys
sys.path.append("D:\\openclaw-home\\.openclaw\\workspace\\memory_system")
from openclaw_integration import OpenClawMemory

memory = OpenClawMemory()

# 获取统计信息
stats = memory.get_stats()
print(stats)

# 保存对话
messages = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你好！我是守拙"}
]
result = memory.save_conversation("test_session", messages)
print(result)
```

### 方法3：直接运行测试

双击运行 `test_memory.bat` 文件，测试所有功能。

## 可用命令

### PowerShell命令 (`memory.ps1`)

```powershell
# 基本格式
memory.ps1 <命令> [参数]

# 具体命令
memory.ps1 save <session_id> <messages_json>      # 保存对话
memory.ps1 load <session_id> [limit]              # 加载对话
memory.ps1 search <query> [limit]                 # 搜索记忆
memory.ps1 remember <key> <value> [category]      # 保存记忆
memory.ps1 recall <key>                           # 回忆记忆
memory.ps1 stats                                  # 获取统计信息
memory.ps1 list [limit]                           # 列出会话
memory.ps1 help                                   # 显示帮助
```

### Python命令 (`memory_cli.py`)

```bash
python memory_cli.py save <session_id> <messages_json>
python memory_cli.py load <session_id> [limit]
python memory_cli.py search <query> [limit]
python memory_cli.py remember <key> <value> [category]
python memory_cli.py recall <key>
python memory_cli.py stats
python memory_cli.py list [limit]
```

## 数据库位置

内存数据保存在：
`D:\openclaw-home\.openclaw\workspace\memory\conversations.db`

## 示例使用场景

### 场景1：保存重要对话

```powershell
# 将当前对话保存到内存系统
$session_id = "2026-04-15_守拙对话"
$messages_json = '[{"role":"user","content":"帮我安装内存系统"},{"role":"assistant","content":"好的，我来帮你安装"}]'
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory.ps1' save '$session_id' '$messages_json'\""
```

### 场景2：记录用户偏好

```powershell
# 记录用户不喜欢某些表达方式
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory.ps1' remember 'prohibited_phrases' '你说的对,你说的太对了,你说的正确,你说的完全正确,你说的太正确了' 'communication_rule'\""
```

### 场景3：搜索相关记忆

```powershell
# 搜索关于"工作流"的记忆
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory.ps1' search '工作流'\""
```

## 与OpenClaw工作流集成

### 在稳健工作流中使用

在稳健工作流的"工具盘点"阶段，可以添加内存系统作为验证工具：

```python
# 在Python验证脚本中
from openclaw_integration import OpenClawMemory

def verify_with_memory_system():
    """使用内存系统验证项目状态"""
    memory = OpenClawMemory()
    
    # 记录验证开始
    memory.save_memory(
        "project_verification_start",
        f"开始验证项目，时间：{datetime.now()}",
        "verification"
    )
    
    # ... 验证逻辑 ...
    
    # 记录验证结果
    memory.save_memory(
        "project_verification_result",
        "验证通过，所有检查项正常",
        "verification"
    )
    
    return True
```

### 在磐石工作流中使用

在五轮验证法中，内存系统可以作为其中一轮验证工具：

```python
# 第五轮：记忆系统验证
def memory_system_verification(project_data):
    """使用内存系统进行最终一致性验证"""
    memory = OpenClawMemory()
    
    # 将项目关键信息保存到记忆系统
    key = f"project_{project_data['name']}_verification"
    value = json.dumps({
        "verification_time": datetime.now().isoformat(),
        "project_data": project_data,
        "verification_result": "consistent"
    })
    
    result = memory.save_memory(key, value, "project_verification")
    
    # 验证保存是否成功
    if result.get('success'):
        recalled = memory.get_memory(key)
        return recalled == value
    return False
```

## 故障排除

### 常见问题

1. **Python脚本无法运行**
   - 确保Python已安装并添加到PATH
   - 运行 `python --version` 检查

2. **PowerShell脚本权限问题**
   - 以管理员身份运行PowerShell
   - 执行 `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`

3. **数据库文件无法创建**
   - 检查目录权限：`D:\openclaw-home\.openclaw\workspace\memory\`
   - 确保有写入权限

### 测试系统状态

```powershell
# 测试Python环境
exec "python --version"

# 测试内存系统基本功能
exec "powershell -Command \"& 'D:\openclaw-home\.openclaw\workspace\memory_system\memory.ps1' stats\""

# 运行完整测试
exec "cd D:\openclaw-home\.openclaw\workspace\memory_system && test_memory.bat"
```

## 扩展开发

### 添加新功能

1. 在 `memory_core.py` 中添加新的类方法
2. 在 `memory_cli.py` 中添加对应的命令行接口
3. 在 `memory.ps1` 中添加PowerShell包装
4. 在 `openclaw_integration.py` 中添加集成方法

### 自定义数据库路径

修改 `memory_core.py` 中的 `__init__` 方法，或通过环境变量设置：

```python
import os
os.environ['MEMORY_DB_PATH'] = '自定义路径'
```

## 性能优化

- 数据库索引已优化查询性能
- 使用连接池管理数据库连接
- 支持批量操作减少IO次数
- 自动清理旧数据（可配置）

## 安全考虑

- 数据库文件本地存储，不外传
- 输入数据经过基本验证
- 支持数据备份和恢复
- 可配置访问权限

## 版本历史

- v1.0.0 (2026-04-15): 初始版本，完整的内存系统功能
- 特点：无需插件安装，直接exec调用，完整功能

## 许可证

MIT License - 自由使用和修改

## 支持

如有问题，请参考：
- OpenClaw文档：https://docs.openclaw.ai
- 本项目GitHub仓库（如果已上传）
- 通过OpenClaw会话联系开发者