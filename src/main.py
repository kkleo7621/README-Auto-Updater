import ast
import os
import re
import argparse
from typing import List, Dict

def parse_python_file(file_path: str) -> List[Dict[str, str]]:
    """
    使用 AST 解析 Python 檔案並提取函數與類別的資訊。
    """
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    metadata = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            metadata.append({
                "type": "function",
                "name": node.name,
                "docstring": ast.get_docstring(node) or "No docstring provided."
            })
        elif isinstance(node, ast.ClassDef):
            metadata.append({
                "type": "class",
                "name": node.name,
                "docstring": ast.get_docstring(node) or "No docstring provided."
            })
    return metadata

def generate_doc_section(metadata: List[Dict[str, str]]) -> str:
    """
    目前暫時手動生成文檔結構，未來這裡將整合 OpenAI API。
    """
    lines = ["| 名稱 | 類型 | 說明 |", "| --- | --- | --- |"]
    for item in metadata:
        doc = item['docstring'].split('\n')[0] # 僅取第一行作為摘要
        lines.append(f"| `{item['name']}` | {item['type']} | {doc} |")
    return "\n".join(lines)

def update_readme(readme_path: str, new_content: str, marker_name: str = "AI-DOC"):
    """
    替換 README.md 中指定標記間的內容。
    """
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = f"<!-- {marker_name}-START -->"
    end_marker = f"<!-- {marker_name}-END -->"

    pattern = rf"{re.escape(start_marker)}.*?{re.escape(end_marker)}"
    replacement = f"{start_marker}\n\n{new_content}\n\n{end_marker}"

    if re.search(pattern, content, re.DOTALL):
        updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print(f"成功更新 {readme_path}")
    else:
        print(f"找不到標記: {start_marker} 或 {end_marker}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="README Auto-Updater")
    parser.add_argument("--file", help="要解析的代碼路徑")
    parser.add_argument("--readme", default="README.md", help="要更新的 README 路徑")
    args = parser.parse_args()

    if args.file and os.path.exists(args.file):
        meta = parse_python_file(args.file)
        doc = generate_doc_section(meta)
        update_readme(args.readme, doc)
    else:
        print("請提供有效的代碼路徑。")
