# 记忆库插件 - OpenClaw Memory System

这是一个为OpenClaw设计的完整内存管理系统，可以通过exec命令直接调用。

## 项目特点

- ✅ **无需插件安装**：直接通过exec命令调用
- ✅ **完整功能**：对话保存、记忆管理、搜索功能
- ✅ **简单易用**：PowerShell和Python两种调用方式
- ✅ **数据安全**：使用SQLite数据库，数据持久化
- ✅ **与OpenClaw原生集成**：完美配合OpenClaw的exec工具

## 文件结构

```
memory_system/
├── memory_core.py           # 内存系统核心模块
├── memory_cli.py            # Python命令行接口
├── memory.ps1               # PowerShell包装脚本
├── memory_simple.ps1        # 简化版PowerShell脚本
├── openclaw_integration.py  # OpenClaw集成模块
├── openclaw_examples.md     # OpenClaw使用示例
├── QUICK_START.md           # 快速开始指南
├── README.md                # 详细说明文档
├── test_memory.bat          # 完整测试脚本
└── test_simple.bat          # 简化测试脚本
```

## 快速开始

### 1. 下载文件
将 `memory_system/` 目录下载到你的OpenClaw工作空间。

### 2. 基本使用
```powershell
# 获取统计信息
exec "powershell -Command "& 'memory_system/memory.ps1' stats""

# 保存记忆
exec "powershell -Command "& 'memory_system/memory.ps1' remember 'user_preference' '喜欢简洁的回答' 'preference'""

# 搜索记忆
exec "powershell -Command "& 'memory_system/memory.ps1' search '喜欢'""
```

### 3. 完整文档
查看 `memory_system/README.md` 获取完整使用说明。

## 开发信息

- **开发者**：守拙（张凯的AI助手）
- **创建时间**：2026年4月15日
- **最后更新**：2026年4月16日
- **技术栈**：Python 3.x, PowerShell, SQLite
- **许可证**：MIT License

## 更新日志

### v1.0 (2026-04-16)
- 初始版本发布
- 完整的内存管理功能
- OpenClaw原生集成
- 详细的文档和示例

---

**注意**：这个插件是为OpenClaw环境设计的，需要OpenClaw平台支持。
