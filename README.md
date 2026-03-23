# README Auto-Updater 🚀

[![OpenAI OSS Badge](https://img.shields.io/badge/OpenAI-OSS%20Codex-blue)](https://openai.com/zh-Hant/form/codex-for-oss/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**README Auto-Updater** 是一個利用 AI 技術自動同步代碼變動至文檔的小工具。它能精準解析您的源代碼，並在 `README.md` 中自動生成與更新函數、類別的詳細說明。

## 🌟 核心特色

- **AI 驅動**：使用 GPT-4o 系列模型，生成高品質、人類可讀的文檔。
- **無縫整合**：只需在 README 中加入簡單的標籤，即可實現局部更新，不影響手寫內容。
- **支援多語言**：目前初步支援 Python (AST 解析)，計畫擴展至 JavaScript/TypeScript。
- **GitHub Action**：支援 CI/CD 自動化流程。

## 🛠️ 安裝說明

```bash
git clone https://github.com/your-username/README-Auto-Updater.git
cd README-Auto-Updater
pip install -r requirements.txt
```

## 📖 使用範例

在您的 `README.md` 檔案中加入以下標記：

<!-- AI-DOC-START -->

| 名稱 | 類型 | 說明 |
| --- | --- | --- |
| `factorial` | function | 計算 n 的階乘。 |
| `Calculator` | class | 提供基礎數學運算的計算機類別。 |
| `add` | function | 將兩個數字相加。 |

<!-- AI-DOC-END -->

然後執行以下指令：

```bash
python src/main.py --file your_script.py --readme README.md
```

## 🏗️ 系統架構

<!-- AI-DOC-START:ARCH -->
(AI 將在這裡更新代碼結構摘要)
<!-- AI-DOC-END:ARCH -->

## 📄 授權協議

本專案採用 [MIT License](LICENSE) 授權。
