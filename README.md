# 🤖 README Auto-Updater

> **Keep your project documentation in sync with your code, effortlessly.**
> **讓您的開源專案文檔與代碼永不脫節。**

[![GitHub Stars](https://img.shields.io/github/stars/kkleo7621/README-Auto-Updater?style=for-the-badge)](https://github.com/kkleo7621/README-Auto-Updater/stargazers)
[![OpenAI OSS](https://img.shields.io/badge/OpenAI-OSS%20Codex-blue?style=for-the-badge)](https://openai.com/zh-Hant/form/codex-for-oss/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## 💡 Why README Auto-Updater? / 為什麼需要它？

Writing documentation is tedious, and it often becomes outdated as code evolves. **README Auto-Updater** uses AI and AST parsing to monitor your code changes and automatically refreshes API descriptions in your README every time you commit.

手寫文檔很累，且一旦代碼更新，文檔往往會過時。**README Auto-Updater** 透過 AI 與 AST 解析技術，自動監控您的代碼變動，並在您提交代碼時，自動重新整理 README 中的 API 說明。

### 🌟 Shocking "Before & After" / 震撼的「前後對比」

| Before (Outdated) / 變更前 | After (Synced) / 變更後 |
| :--- | :--- |
| ❌ Shows old parameter `data` / 顯示舊參數 | ✅ Auto-updated to `payload: Dict` / 自動更新 |
| ❌ Missing new `validate()` function / 缺少新函數 | ✅ `validate()` added automatically / 自動補齊 |

---

## 🚀 Quick Start / 快速上手

Get started in three simple steps: / 只需三步，即可為您的專案啟用自動化文檔：

### 1. Add Sync Markers / 植入同步標籤
Place these markers in your `README.md` where you want the API docs to appear: / 在您想要顯示 API 文檔的地方放入以下標記：

```markdown
[AI-DOC-START]
<!-- 文檔將在此生成 -->
[AI-DOC-END]
```

### 2. Run Local Test / 本地執行測試
```bash
python src/main.py --file src/main.py --readme README.md
```

### 3. Integrate GitHub Action / 加入 GitHub Action
Use our [auto-doc.yml](.github/workflows/auto-doc.yml) in your repository to keep docs updated on every push! / 使用我們提供的流程，每次 `git push` 都會自動更新！

---

## 🛠️ Current API Reference / 目前解析紀錄

<!-- AI-DOC-START -->

| Name / 名稱 | Type / 類型 | Signature / 簽名 | Description / 說明 |
| --- | --- | --- | --- |
| `DataProcessor` | **class** | - | A utility class for processing and cleaning dataset-like structures. |
| `SecureLogger` | **class** | - | Handles encrypted logging for sensitive operations. |
| `format_date` | **function** | `(timestamp)` | Converts a unix timestamp to a human-readable string. |
| `__init__` | **function** | `(self, data_source)` | Initialize with a data source path. |
| `clean_records` | **function** | `(self, raw_data)` | Removes duplicates and null values from raw data. |
| `export_csv` | **function** | `(self, filename)` | Exports the processed data to a CSV file. |
| `log_event` | **function** | `(self, level, message)` | Logs a message with a specific severity level. |
| `parse_python_file` | **function** | `(file_path)` | 使用 AST 解析 Python 檔案並提取函數與類別的資訊。 |
| `generate_doc_section` | **function** | `(metadata)` | 生成更專業的 Markdown 表格。 |
| `update_readme` | **function** | `(readme_path, new_content, marker_name)` | 替換 README.md 中指定標記間的內容。 |

<!-- AI-DOC-END -->

---

## 🗺️ Roadmap / 開發路線圖
- [x] Python AST parsing / Python AST 基礎解析
- [x] GitHub Action automation / GitHub Action 自動化同步
- [ ] GPT-4o integration / 整合 GPT-4o 生成人性化摘要
- [ ] JS / TS support / 支援 JavaScript / TypeScript 解析
- [ ] Custom Markdown templates / 支援自定義模板

## 📄 License / 授權協議
This project is licensed under the [MIT License](LICENSE). / 本專案採用 MIT 授權。
