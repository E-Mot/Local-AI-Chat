# 🎓 Local Desktop AI Chat

A local desktop AI chat application built with Python, Tkinter, and Ollama. 

This project allows me to interact with a locally hosted large language model (LLM) while deepening my understanding of Python application design, UI development, and AI integration as an IT student.

---

## 🗂 Project Structure

```
LocalAIChat/
│
├── .venv
│ 
├── app_logic.py          # LLM interaction & streaming logic
├── main_ui.py            # Tkinter UI and application logic
├── version.py            # Application version (SemVer)
│
├── requirements.txt      # Project dependencies for recreating the venv
├── README.md             # Project documentation
│
├── .gitignore            # Excludes venv, cache, build artifacts, etc.
│
├── logo.ico              # Application icon
├── logo.png              # AI avatar image
└── user.png              # User avatar image

```

### 📦 Build Artifacts (Generated Later)

These folders and files are created when running PyInstaller:

```
LocalAIChat/
│
├── build/                    # PyInstaller build artifacts (auto-generated)
├── dist/                     # Packaged executable output
└── LocalAIChat.spec          # PyInstaller spec file for executable configuration

```

---

## ✨ Current Features

✅ Local LLM chat using Ollama

✅ Streaming AI responses (typing effect)

✅ Tkinter-based chat interface

✅ Chat bubbles with user/AI separation

✅ Scrollable conversation history

✅ Responsive resizing behavior

✅ Can be packaged into a single `.exe` for Windows (using PyInstaller)

---

## 🚀 How It Works

### 1️⃣ Prerequisites

- Ollama installed and running locally  
  👉 https://ollama.com

Pull the model:

```bash
ollama pull qwen2.5:7b
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Application

```bash
python main_ui.py
```

---

## 🧩 Requirements & Dependencies

### 📚 Python Version and Libraries

- Python **3.10+**
- **ollama** — Local LLM interaction and streaming
- **Pillow** — Image handling for the Tkinter UI

All other imports are part of Python’s standard library.

Optional (for packaging):
```bash
pip install pyinstaller
```

### 🤖 Model Information

- **Model**: `qwen2.5:7b`  
- Models can be swapped easily by changing the model name in `app_logic.py`

---

## 🏗️ Building the Executable

To package the project into a standalone `.exe` (for Windows):

```bash
pyinstaller --onefile --clean --noconsole --icon=logo.ico --add-data "logo.png;." --add-data "user.png;." --name LocalAIChat app_ui.py
```

The executable will appear in the `dist/` folder as:
```
LocalAIChat.exe
```

You can then run:
```bash
LocalAIChat.exe
```

---

## 🧭 Versioning

Version information is stored in `version.py` and follows the **Semantic Versioning (SemVer)** standard:

```
MAJOR.MINOR.PATCH
```

| Segment | Meaning |
|----------|----------|
| **MAJOR** | Incompatible or breaking changes |
| **MINOR** | New features or major enhancements |
| **PATCH** | Bug fixes or small improvements |

Current version:
```
v0.1.0 — Early-stage version of the program
```

---

## 💡 Future Plans

- [ ] Long-Term Memory
- [ ] Image Generation
- [ ] Conversation Management
- [ ] UI Customization Options

---

## 🧠 Learning Outcomes

This project demonstrates:

- Practical application of Python programming concepts
- Modular software design across multiple Python files
- Development of a graphical user interface (GUI) using Tkinter
- Event-driven programming and user input handling
- Multithreading for responsive GUI applications
- Streaming and real-time display of AI-generated output
- Integration with external APIs and libraries (Ollama, Pillow)
- Dependency management using virtual environments
- Packaging a Python application into a standalone executable with PyInstaller
- Use of semantic versioning (SemVer) for release tracking
- Clear technical documentation using Markdown
- Iterative UI/UX refinement through hands-on testing

---

## 👤 Author

**Emmanuel Mot**  
Information Technology Major — Web and Software Development  
Purdue University Global  

---

## 📝 License

This project is intended for **educational and personal use**.  
You are free to modify or expand it for your own learning purposes.

---

### ⭐ Acknowledgements

Special thanks to open-source developers and documentation writers whose tools make learning and experimentation possible.

---