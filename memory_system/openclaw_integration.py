#!/usr/bin/env python3
"""
OpenClaw 内存系统集成模块
提供与OpenClaw exec命令集成的功能
"""

import subprocess
import json
import os

class OpenClawMemory:
    """OpenClaw内存系统集成类"""
    
    def __init__(self, workspace_path=None):
        """初始化
        
        Args:
            workspace_path: OpenClaw工作空间路径
        """
        if workspace_path is None:
            self.workspace_path = "D:\\openclaw-home\\.openclaw\\workspace"
        else:
            self.workspace_path = workspace_path
        
        self.memory_script = os.path.join(self.workspace_path, "memory_system", "memory.ps1")
    
    def _run_command(self, command, *args):
        """运行内存系统命令
        
        Args:
            command: 命令名称
            *args: 命令参数
            
        Returns:
            命令输出（JSON字符串）
        """
        try:
            # 构建命令
            cmd_args = ["powershell", "-Command", f"& '{self.memory_script}' {command}"]
            cmd_args.extend(args)
            
            # 执行命令
            result = subprocess.run(
                cmd_args,
                capture_output=True,
                text=True,
                cwd=self.workspace_path
            )
            
            if result.returncode != 0:
                return json.dumps({'error': result.stderr})
            
            return result.stdout.strip()
        
        except Exception as e:
            return json.dumps({'error': str(e)})
    
    def save_conversation(self, session_id, messages):
        """保存对话
        
        Args:
            session_id: 会话ID
            messages: 消息列表
            
        Returns:
            保存结果
        """
        messages_json = json.dumps(messages, ensure_ascii=False)
        output = self._run_command("save", session_id, f'"{messages_json}"')
        try:
            return json.loads(output)
        except:
            return {'error': output}
    
    def load_conversation(self, session_id, limit=100):
        """加载对话
        
        Args:
            session_id: 会话ID
            limit: 最大消息数量
            
        Returns:
            消息列表
        """
        output = self._run_command("load", session_id, str(limit))
        try:
            result = json.loads(output)
            return result.get('messages', [])
        except:
            return []
    
    def search_memories(self, query, limit=10):
        """搜索记忆
        
        Args:
            query: 搜索关键词
            limit: 最大结果数量
            
        Returns:
            搜索结果
        """
        output = self._run_command("search", query, str(limit))
        try:
            result = json.loads(output)
            return result.get('results', [])
        except:
            return []
    
    def save_memory(self, key, value, category="general"):
        """保存记忆
        
        Args:
            key: 记忆键
            value: 记忆值
            category: 分类
            
        Returns:
            保存结果
        """
        output = self._run_command("remember", key, value, category)
        try:
            return json.loads(output)
        except:
            return {'error': output}
    
    def get_memory(self, key):
        """获取记忆
        
        Args:
            key: 记忆键
            
        Returns:
            记忆值
        """
        output = self._run_command("recall", key)
        try:
            result = json.loads(output)
            return result.get('value')
        except:
            return None
    
    def get_stats(self):
        """获取统计信息
        
        Returns:
            统计信息
        """
        output = self._run_command("stats")
        try:
            return json.loads(output)
        except:
            return {'error': output}
    
    def list_sessions(self, limit=20):
        """列出会话
        
        Args:
            limit: 最大会话数量
            
        Returns:
            会话列表
        """
        output = self._run_command("list", str(limit))
        try:
            result = json.loads(output)
            return result.get('sessions', [])
        except:
            return []


# 示例使用
if __name__ == '__main__':
    memory = OpenClawMemory()
    
    print("=== OpenClaw 内存系统集成测试 ===")
    print()
    
    # 测试统计信息
    print("1. 获取统计信息:")
    stats = memory.get_stats()
    print(json.dumps(stats, indent=2, ensure_ascii=False))
    print()
    
    # 测试保存记忆
    print("2. 保存测试记忆:")
    result = memory.save_memory("test_key", "这是一个通过OpenClaw集成的测试记忆", "test")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print()
    
    # 测试获取记忆
    print("3. 获取测试记忆:")
    value = memory.get_memory("test_key")
    print(f"记忆值: {value}")
    print()
    
    # 测试搜索记忆
    print("4. 搜索记忆:")
    results = memory.search_memories("测试")
    print(json.dumps(results, indent=2, ensure_ascii=False))
    print()
    
    print("测试完成!")