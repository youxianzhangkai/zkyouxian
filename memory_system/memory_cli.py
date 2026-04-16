#!/usr/bin/env python3
"""
OpenClaw 内存系统命令行工具
简化版本，便于通过exec调用
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from memory_core import MemorySystem
import json

def main():
    """简化版命令行接口"""
    if len(sys.argv) < 2:
        print("用法: python memory_cli.py <命令> [参数]")
        print("命令:")
        print("  save <session_id> <messages_json> - 保存对话")
        print("  load <session_id> [limit] - 加载对话")
        print("  search <query> [limit] - 搜索记忆")
        print("  remember <key> <value> [category] - 保存记忆")
        print("  recall <key> - 回忆记忆")
        print("  stats - 获取统计信息")
        print("  list [limit] - 列出会话")
        return
    
    command = sys.argv[1]
    memory = MemorySystem()
    
    try:
        if command == 'save':
            if len(sys.argv) < 4:
                print("错误: save命令需要session_id和messages_json参数")
                return
            session_id = sys.argv[2]
            messages_json = sys.argv[3]
            messages = json.loads(messages_json)
            success = memory.save_conversation(session_id, messages)
            print(json.dumps({'success': success}))
        
        elif command == 'load':
            if len(sys.argv) < 3:
                print("错误: load命令需要session_id参数")
                return
            session_id = sys.argv[2]
            limit = int(sys.argv[3]) if len(sys.argv) > 3 else 100
            messages = memory.load_conversation(session_id, limit)
            print(json.dumps({'messages': messages}))
        
        elif command == 'search':
            if len(sys.argv) < 3:
                print("错误: search命令需要query参数")
                return
            query = sys.argv[2]
            limit = int(sys.argv[3]) if len(sys.argv) > 3 else 10
            results = memory.search_memories(query, limit)
            print(json.dumps({'results': results}))
        
        elif command == 'remember':
            if len(sys.argv) < 4:
                print("错误: remember命令需要key和value参数")
                return
            key = sys.argv[2]
            value = sys.argv[3]
            category = sys.argv[4] if len(sys.argv) > 4 else 'general'
            success = memory.save_memory(key, value, category)
            print(json.dumps({'success': success}))
        
        elif command == 'recall':
            if len(sys.argv) < 3:
                print("错误: recall命令需要key参数")
                return
            key = sys.argv[2]
            value = memory.get_memory(key)
            print(json.dumps({'value': value}))
        
        elif command == 'stats':
            stats = memory.get_stats()
            print(json.dumps(stats))
        
        elif command == 'list':
            limit = int(sys.argv[2]) if len(sys.argv) > 2 else 20
            sessions = memory.list_sessions(limit)
            print(json.dumps({'sessions': sessions}))
        
        else:
            print(f"未知命令: {command}")
    
    except Exception as e:
        print(json.dumps({'error': str(e)}))


if __name__ == '__main__':
    main()