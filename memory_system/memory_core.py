#!/usr/bin/env python3
"""
OpenClaw 内存系统核心模块
一个简单但完整的内存管理系统，可以通过exec命令调用
"""

import sqlite3
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any
import sys

class MemorySystem:
    """内存系统核心类"""
    
    def __init__(self, db_path: str = None):
        """初始化内存系统
        
        Args:
            db_path: SQLite数据库路径，默认为workspace/memory/conversations.db
        """
        if db_path is None:
            # 默认路径
            workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.db_path = os.path.join(workspace_dir, "memory", "conversations.db")
        else:
            self.db_path = db_path
        
        # 确保目录存在
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        # 初始化数据库
        self._init_database()
    
    def _init_database(self):
        """初始化数据库表结构"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # 创建会话表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id TEXT PRIMARY KEY,
            title TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            metadata TEXT DEFAULT '{}'
        )
        ''')
        
        # 创建消息表
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT,
            role TEXT,
            content TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            metadata TEXT DEFAULT '{}',
            FOREIGN KEY (session_id) REFERENCES sessions (id) ON DELETE CASCADE
        )
        ''')
        
        # 创建记忆表（长期记忆）
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE,
            value TEXT,
            category TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            metadata TEXT DEFAULT '{}'
        )
        ''')
        
        # 创建索引
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_messages_session ON messages(session_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_messages_timestamp ON messages(timestamp)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_memories_key ON memories(key)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_memories_category ON memories(category)')
        
        conn.commit()
        conn.close()
    
    def save_conversation(self, session_id: str, messages: List[Dict]) -> bool:
        """保存对话记录
        
        Args:
            session_id: 会话ID
            messages: 消息列表，每个消息包含role和content
            
        Returns:
            是否保存成功
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # 更新或创建会话
            cursor.execute('''
            INSERT OR REPLACE INTO sessions (id, title, updated_at)
            VALUES (?, ?, ?)
            ''', (session_id, f"会话 {session_id[:8]}", datetime.now().isoformat()))
            
            # 清空该会话的旧消息
            cursor.execute('DELETE FROM messages WHERE session_id = ?', (session_id,))
            
            # 插入新消息
            for msg in messages:
                cursor.execute('''
                INSERT INTO messages (session_id, role, content, timestamp)
                VALUES (?, ?, ?, ?)
                ''', (session_id, msg.get('role', 'unknown'), 
                      msg.get('content', ''), datetime.now().isoformat()))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"保存对话失败: {e}", file=sys.stderr)
            return False
    
    def load_conversation(self, session_id: str, limit: int = 100) -> List[Dict]:
        """加载对话记录
        
        Args:
            session_id: 会话ID
            limit: 最大消息数量
            
        Returns:
            消息列表
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
            SELECT role, content, timestamp 
            FROM messages 
            WHERE session_id = ? 
            ORDER BY timestamp ASC 
            LIMIT ?
            ''', (session_id, limit))
            
            messages = []
            for row in cursor.fetchall():
                messages.append({
                    'role': row[0],
                    'content': row[1],
                    'timestamp': row[2]
                })
            
            conn.close()
            return messages
        except Exception as e:
            print(f"加载对话失败: {e}", file=sys.stderr)
            return []
    
    def search_memories(self, query: str, limit: int = 10) -> List[Dict]:
        """搜索记忆
        
        Args:
            query: 搜索关键词
            limit: 最大结果数量
            
        Returns:
            记忆列表
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # 简单搜索：在key或value中包含查询词
            cursor.execute('''
            SELECT key, value, category, updated_at 
            FROM memories 
            WHERE key LIKE ? OR value LIKE ? 
            ORDER BY updated_at DESC 
            LIMIT ?
            ''', (f'%{query}%', f'%{query}%', limit))
            
            results = []
            for row in cursor.fetchall():
                results.append({
                    'key': row[0],
                    'value': row[1],
                    'category': row[2],
                    'updated_at': row[3]
                })
            
            conn.close()
            return results
        except Exception as e:
            print(f"搜索记忆失败: {e}", file=sys.stderr)
            return []
    
    def save_memory(self, key: str, value: str, category: str = "general") -> bool:
        """保存记忆
        
        Args:
            key: 记忆键
            value: 记忆值
            category: 分类
            
        Returns:
            是否保存成功
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
            INSERT OR REPLACE INTO memories (key, value, category, updated_at)
            VALUES (?, ?, ?, ?)
            ''', (key, value, category, datetime.now().isoformat()))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"保存记忆失败: {e}", file=sys.stderr)
            return False
    
    def get_memory(self, key: str) -> Optional[str]:
        """获取记忆
        
        Args:
            key: 记忆键
            
        Returns:
            记忆值，如果不存在则返回None
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('SELECT value FROM memories WHERE key = ?', (key,))
            row = cursor.fetchone()
            
            conn.close()
            return row[0] if row else None
        except Exception as e:
            print(f"获取记忆失败: {e}", file=sys.stderr)
            return None
    
    def list_sessions(self, limit: int = 20) -> List[Dict]:
        """列出所有会话
        
        Args:
            limit: 最大会话数量
            
        Returns:
            会话列表
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
            SELECT id, title, created_at, updated_at 
            FROM sessions 
            ORDER BY updated_at DESC 
            LIMIT ?
            ''', (limit,))
            
            sessions = []
            for row in cursor.fetchall():
                # 获取每个会话的消息数量
                cursor.execute('SELECT COUNT(*) FROM messages WHERE session_id = ?', (row[0],))
                msg_count = cursor.fetchone()[0]
                
                sessions.append({
                    'id': row[0],
                    'title': row[1],
                    'created_at': row[2],
                    'updated_at': row[3],
                    'message_count': msg_count
                })
            
            conn.close()
            return sessions
        except Exception as e:
            print(f"列出会话失败: {e}", file=sys.stderr)
            return []
    
    def get_stats(self) -> Dict[str, Any]:
        """获取统计信息
        
        Returns:
            统计信息字典
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # 会话数量
            cursor.execute('SELECT COUNT(*) FROM sessions')
            session_count = cursor.fetchone()[0]
            
            # 消息总数
            cursor.execute('SELECT COUNT(*) FROM messages')
            message_count = cursor.fetchone()[0]
            
            # 记忆数量
            cursor.execute('SELECT COUNT(*) FROM memories')
            memory_count = cursor.fetchone()[0]
            
            # 数据库大小
            db_size = os.path.getsize(self.db_path) if os.path.exists(self.db_path) else 0
            
            conn.close()
            
            return {
                'session_count': session_count,
                'message_count': message_count,
                'memory_count': memory_count,
                'db_size_bytes': db_size,
                'db_size_mb': round(db_size / (1024 * 1024), 2),
                'status': 'healthy'
            }
        except Exception as e:
            print(f"获取统计信息失败: {e}", file=sys.stderr)
            return {'status': 'error', 'error': str(e)}


def main():
    """命令行接口"""
    import argparse
    
    parser = argparse.ArgumentParser(description='OpenClaw 内存系统')
    subparsers = parser.add_subparsers(dest='command', help='命令')
    
    # save 命令
    save_parser = subparsers.add_parser('save', help='保存对话')
    save_parser.add_argument('session_id', help='会话ID')
    save_parser.add_argument('--messages', required=True, help='JSON格式的消息列表')
    
    # load 命令
    load_parser = subparsers.add_parser('load', help='加载对话')
    load_parser.add_argument('session_id', help='会话ID')
    load_parser.add_argument('--limit', type=int, default=100, help='最大消息数量')
    
    # search 命令
    search_parser = subparsers.add_parser('search', help='搜索记忆')
    search_parser.add_argument('query', help='搜索关键词')
    search_parser.add_argument('--limit', type=int, default=10, help='最大结果数量')
    
    # remember 命令
    remember_parser = subparsers.add_parser('remember', help='保存记忆')
    remember_parser.add_argument('key', help='记忆键')
    remember_parser.add_argument('value', help='记忆值')
    remember_parser.add_argument('--category', default='general', help='分类')
    
    # recall 命令
    recall_parser = subparsers.add_parser('recall', help='回忆记忆')
    recall_parser.add_argument('key', help='记忆键')
    
    # stats 命令
    stats_parser = subparsers.add_parser('stats', help='获取统计信息')
    
    # list 命令
    list_parser = subparsers.add_parser('list', help='列出会话')
    list_parser.add_argument('--limit', type=int, default=20, help='最大会话数量')
    
    args = parser.parse_args()
    
    memory = MemorySystem()
    
    if args.command == 'save':
        try:
            messages = json.loads(args.messages)
            success = memory.save_conversation(args.session_id, messages)
            print(json.dumps({'success': success}))
        except json.JSONDecodeError:
            print(json.dumps({'success': False, 'error': '无效的JSON格式'}))
    
    elif args.command == 'load':
        messages = memory.load_conversation(args.session_id, args.limit)
        print(json.dumps({'messages': messages}))
    
    elif args.command == 'search':
        results = memory.search_memories(args.query, args.limit)
        print(json.dumps({'results': results}))
    
    elif args.command == 'remember':
        success = memory.save_memory(args.key, args.value, args.category)
        print(json.dumps({'success': success}))
    
    elif args.command == 'recall':
        value = memory.get_memory(args.key)
        print(json.dumps({'value': value}))
    
    elif args.command == 'stats':
        stats = memory.get_stats()
        print(json.dumps(stats))
    
    elif args.command == 'list':
        sessions = memory.list_sessions(args.limit)
        print(json.dumps({'sessions': sessions}))
    
    else:
        parser.print_help()


if __name__ == '__main__':
    main()