# 🗣️ Talky



**Talky** is a lightweight command-line AI chat tool that lets you interact with an AI model directly from your terminal.  
Minimal by design, it’s perfect for quick questions, code generation, prototyping ideas, or integrating AI into your developer workflow.

---
## 🎬 Demo

[![Play demo (click to open)](./demo-thumbnail.png)](./demo.mov)

> Note: GitHub does not play .mov files inline. Convert to GIF or MP4 for an inline preview, or link to the file.

If you have a GIF:
![Demo GIF](./demo.gif)

Or provide a direct link:
[Open demo.mov](./demo.mov) · [Open demo.mp4](./demo.mp4)

Quick conversion examples (ffmpeg):
```bash
# Convert to MP4 (recommended)
ffmpeg -i demo.mov -c:v libx264 -crf 23 -preset medium demo.mp4

# Convert to GIF for inline preview
ffmpeg -i demo.mov -vf "fps=15,scale=680:-1:flags=lanczos" -loop 0 demo.gif
```


## 🚀 Features

- 💬 Chat with an AI assistant directly from your terminal  
- ⚡ Lightweight and fast – no unnecessary dependencies  
- 🧠 Great for coding help, explanations, and automation  
- 🔌 Easy setup with your own API key  
- 🧩 Simple to extend and integrate into scripts

---

## 🛠️ Installation

Clone the repository and install dependencies (if any):

```bash
git https://github.com/Moataz0000/CLI-AI-Chat

pip install -r requirements.txt

python3 talky.py
