# 🤖 README Auto-Updater

> **讓您的開源專案文檔與代碼永不脫節。**

[![GitHub Stars](https://img.shields.io/github/stars/kkleo7621/README-Auto-Updater?style=for-the-badge)](https://github.com/kkleo7621/README-Auto-Updater/stargazers)
[![OpenAI OSS](https://img.shields.io/badge/OpenAI-OSS%20Codex-blue?style=for-the-badge)](https://openai.com/zh-Hant/form/codex-for-oss/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## 💡 為什麼需要它？

手寫文檔很累，且一旦代碼更新，文檔往往會過時。**README Auto-Updater** 透過 AI 與 AST 解析技術，自動監控您的代碼變動，並在您提交代碼時，自動重新整理 README 中的 API 說明。

### 🌟 震撼的「前後對比」

| 變更前 (代碼更新後文檔沒動) | 變更後 (使用本工具同步後) |
| :--- | :--- |
| ❌ 文檔顯示舊參數 `data` | ✅ 文檔自動更新為 `payload: Dict` 選項 |
| ❌ 缺少新加入的 `validate()` 函數 | ✅ 自動偵測並補上 `validate()` 說明表格 |

---

## 🚀 快速上手 (Usage)

只需三步，即可為您的專案啟用自動化文檔：

### 1. 植入同步標籤
在您的 `README.md` 想要顯示 API 文檔的地方放入以下標記：

```markdown
<!-- AI-DOC-START -->

| 名稱 | 類型 | 參數 / 簽名 | 說明 |
| --- | --- | --- | --- |
| `parse_python_file` | **function** | `(file_path)` | 使用 AST 解析 Python 檔案並提取函數與類別的資訊。 |
| `generate_doc_section` | **function** | `(metadata)` | 生成更專業的 Markdown 表格。 |
| `update_readme` | **function** | `(readme_path, new_content, marker_name)` | 替換 README.md 中指定標記間的內容。 |

<!-- AI-DOC-END -->
```

### 2. 本地執行測試
```bash
# 自動掃描 src/main.py 並同步到 README.md
python src/main.py --file src/main.py --readme README.md
```

### 3. 加入 GitHub Action (推薦)
將本專案提供的 [auto-doc.yml](.github/workflows/auto-doc.yml) 放入您的儲存庫，每次 `git push` 時，AI 都會幫您檢查並更新文檔！

---

## 🛠️ 目前解析紀錄

<!-- AI-DOC-START -->

| 名稱 | 類型 | 參數 / 簽名 | 說明 |
| --- | --- | --- | --- |
| `parse_python_file` | **function** | `(file_path)` | 使用 AST 解析 Python 檔案並提取函數與類別的資訊。 |
| `generate_doc_section` | **function** | `(metadata)` | 生成更專業的 Markdown 表格。 |
| `update_readme` | **function** | `(readme_path, new_content, marker_name)` | 替換 README.md 中指定標記間的內容。 |

<!-- AI-DOC-END -->

---

## 🗺️ 開發路線圖 (Roadmap)
- [x] Python AST 基礎解析系統
- [x] GitHub Action 自動化同步流程
- [ ] 整合 GPT-4o 生成更人性化的函數摘要
- [ ] 支援 JavaScript / TypeScript 解析
- [ ] 支援自定義 Markdown 模板生成

## 📄 授權協議
本專案採用 [MIT License](LICENSE) 授權。
