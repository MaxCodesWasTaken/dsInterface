# GGUF Chat Interface (LLM Loader with `llama.cpp` + `llama-cpp-python`)

This is a lightweight Python-based chat interface for interacting with local LLMs using the [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) bindings. It supports any compatible `.gguf` model and provides a simple terminal UI using the `rich` library.

---

## Features

- Auto-scans the `models/` folder for available `.gguf` models.
- Lets the user choose the model interactively.
- Provides a streaming chat interface with rich formatting.
- Shows token generation stats after each response.

---

## Requirements

Install dependencies with:

```bash
pip install llama-cpp-python rich
```

Note: You must have a working C++ backend or use the included llama.cpp repo (optional, see submodule instructions below).

## Usage

Clone this repo:

```bash
git clone https://github.com/yourusername/gguf-chat
cd gguf-chat
```
(Optional but recommended) Clone llama.cpp as a submodule:

```bash
git submodule add https://github.com/ggerganov/llama.cpp
```
Add your .gguf models to the models/ directory (this folder is excluded from Git for size/legal reasons).

Run the app:

```bash
python main.py
```

## Project Structure
```bash
.
├── llama.cpp/           # (optional) llama.cpp backend, add as submodule
├── models/              # Place your .gguf model files here (ignored by Git)
│   └── your-model.gguf
├── main.py              # Main chat interface
├── .gitignore
└── README.md
```

## Notes
models/ is excluded from version control. You'll need to manually download and place your .gguf files there.

The app automatically detects and loads one of the models you place in that folder.

You can use models like:

- DeepSeek
- Mistral
- Qwen
- Or any GGUF-compatible model

## Example Models You Can Use
Some models known to work well:

- deepseek-coder-6.7b-instruct.Q4_K_M.gguf
- mistral-7b-instruct-v0.1.Q4_K_M.gguf
- Janus-Pro-7B-LM.Q4_K_M.gguf

Note: Machine used was Intel i7, integrated graphics (again why we used GGUF)

