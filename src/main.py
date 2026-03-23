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
            # 獲取參數列表
            args = [arg.arg for arg in node.args.args]
            arg_str = f"({', '.join(args)})"
            metadata.append({
                "type": "function",
                "name": node.name,
                "signature": arg_str,
                "docstring": ast.get_docstring(node) or "No docstring provided."
            })
        elif isinstance(node, ast.ClassDef):
            metadata.append({
                "type": "class",
                "name": node.name,
                "signature": "",
                "docstring": ast.get_docstring(node) or "No docstring provided."
            })
    return metadata

def generate_doc_section(metadata: List[Dict[str, str]]) -> str:
    """
    生成更專業的 Markdown 表格 / Generate professional Markdown table.
    """
    lines = ["| Name / 名稱 | Type / 類型 | Signature / 簽名 | Description / 說明 |", "| --- | --- | --- | --- |"]
    for item in metadata:
        # 支援多行註解（將雙語內容合併為單行顯示）
        doc_lines = [line.strip() for line in item['docstring'].split('\n') if line.strip()]
        doc = " ".join(doc_lines) if doc_lines else "-"
        sig = f"`{item['signature']}`" if item['signature'] else "-"
        lines.append(f"| `{item['name']}` | **{item['type']}** | {sig} | {doc} |")
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

    if args.file:
        files = [args.file] if os.path.isfile(args.file) else []
        if os.path.isdir(args.file):
            import glob
            files = glob.glob(os.path.join(args.file, "**/*.py"), recursive=True)
        
        all_meta = []
        for f_path in files:
            all_meta.extend(parse_python_file(f_path))
            
        if all_meta:
            doc = generate_doc_section(all_meta)
            update_readme(args.readme, doc)
            print(f"從 {len(files)} 個檔案中提取了 {len(all_meta)} 個項目。")
    else:
        print("請提供有效的代碼路徑 (--file)。")
