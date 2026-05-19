"""
Code Archaeologist - 主入口
当前状态：项目初始化阶段
"""

def parse_codebase(repo_path: str) -> dict:
    """解析代码仓库，提取函数调用关系"""
    # TODO: 使用tree-sitter进行AST解析
    pass

def build_call_graph(parsed_data: dict) -> dict:
    """构建跨文件调用图谱"""
    # TODO: 建立符号索引和调用关系
    pass

def archaeologist_agent(call_graph: dict, query: str) -> str:
    """追踪函数调用链，回答参数来源"""
    # TODO: 接入MiMo API，进行长链推理
    pass

if __name__ == "__main__":
    print("Code Archaeologist - 开发中...")
    print("当前进度：项目骨架搭建完成，下一步实现AST解析模块")