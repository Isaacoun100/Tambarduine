# 🪘 Tambarduine

[![Python](https://img.shields.io/badge/Python-100%25-3776AB?logo=python)](https://www.python.org/)
[![Arduino](https://img.shields.io/badge/Arduino-Firmata-00979D?logo=arduino)](https://www.arduino.cc/)
[![IDE](https://img.shields.io/badge/IDE-Tkinter-2D3748)](https://docs.python.org/3/library/tkinter.html)
[![Status](https://img.shields.io/badge/Status-Academic_Project-yellow)]()

**Tambarduine** is an academic programming project that combines a custom programming language, a graphical IDE, and an Arduino-controlled physical tambourine.

Users can write routines in the `.tmn` language to control:

- 🪘 Tambourine movements
- 🥁 Percussion actions
- 🔄 Vibrato movements
- 💡 Physical LEDs
- ⏱️ A metronome
- 🎵 Musical timing and sequences

The device was built with an Arduino, servo motors, motors, LEDs, and other electronic components. This repository contains the software that translates Tambarduine programs into commands for the hardware.

---

## ✨ Project Overview

The objective of Tambarduine was to create a simple language that allows users to program a remote tambourine without directly manipulating Arduino code.

Instead of writing Python or Arduino instructions, the user writes commands such as:

```text
Vibrato(10, 1)
Percutor(D, 1)
Golpe(1)
```

The IDE processes the source code through:

1. 🔤 Lexical analysis
2. 🌳 Syntax analysis
3. 🌲 Abstract Syntax Tree creation
4. ⚙️ Code generation
5. 🤖 Hardware execution through PyFirmata

---

## 🎯 Features

- 🖥️ Graphical code editor
- 📂 Open and save `.tmn` files
- ▶️ Compile and run routines
- 🧾 Compiler output console
- ⌨️ Fullscreen IDE interface
- 🧩 Custom lexer and parser
- 🌲 Abstract Syntax Tree implementation
- ⚠️ Error and output messages
- 🤖 Arduino communication
- 🔧 Servo motor control
- 💡 LED timing control
- 🥁 Tambourine strike routines
- ⏱️ Metronome functionality
- 🧪 Compiler and message tests
- 🧍 Support for custom demonstration programs

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Main programming language |
| 🖼️ **Tkinter** | Graphical IDE |
| ⚙️ **Sly** | Lexing and parsing support |
| 🤖 **PyFirmata** | Arduino communication |
| 🔧 **Arduino** | Physical device controller |
| 🔄 **Servo motors** | Tambourine movement |
| 💡 **LED** | Visual timing and indicators |
| 🧪 **Unit tests** | Compiler and message testing |

---

## 🤖 Hardware Architecture

```text
┌────────────────────┐
│ Tambarduine IDE    │
│ Python + Tkinter   │
└─────────┬──────────┘
          │ Compile
          ▼
┌────────────────────┐
│  Tambarduine       │
│  Custom Compiler   │
└─────────┬──────────┘
          │ Generated Python
          ▼
┌────────────────────┐
│     PyFirmata      │
│  Board Connection  │
└─────────┬──────────┘
          │ USB / COM Port
          ▼
┌────────────────────┐
│      Arduino       │
│  Digital and Servo │
│       Pins         │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Arduino Tambourine │
│ Motors · Servo · LED│
└────────────────────┘
```

---

## 📁 Project Structure

```text
Tambarduine/
├── compiler/
│   ├── AST/
│   │   ├── AbstractSyntaxTree.py
│   │   └── Node.py
│   ├── Lexic_Analysis/
│   │   ├── Lexer.py
│   │   └── Tokens.py
│   ├── Sintactic_Analysis/
│   │   └── Parser.py
│   ├── Messages/
│   ├── output/
│   └── Compiler.py
├── Firmata/
│   └── Instructions.py
├── GUI/
│   ├── MainWindow.py
│   └── executable.py
├── Prueba/
│   ├── Ejemplos/
│   └── .tmn demonstration programs
├── sly/
├── tests/
├── main.py
├── parser.out
└── README.md
```

---

## 📦 Main Components

### 🖥️ `GUI`

Contains the Tkinter IDE:

- Code editor
- Console
- File open/save controls
- Compile command
- Compile-and-run command
- Fullscreen mode
- Line navigation

The main IDE window is controlled by `GUI/MainWindow.py`.

### 🧩 `compiler`

Contains the complete compiler pipeline:

- Lexical analyzer
- Token definitions
- Syntax parser
- Abstract Syntax Tree
- Code generator
- Error and output messages

The central compiler class is `compiler.Compiler.Comp`.

### 🤖 `Firmata`

Contains the hardware instruction layer.

It controls the Arduino pins and provides methods such as:

- `Percutor`
- `Golpe`
- `Vibrato`
- `Vertical`
- `Abanico`
- `Metronomo`
- `SetServoX`
- `resetServoX`
- `BeepLED`
- `PrenderLED`
- `ApagarLED`

### 🧪 `tests`

Contains tests for:

- Compiler behavior
- Message handling
- Output behavior

### 🎵 `Prueba`

Contains example `.tmn` files demonstrating:

- Left and right movements
- Combined movements
- Vibrato
- Fan movements
- Percussion strikes
- Metronome routines
- Function, syntax, and error tests

---

## 🧠 Compiler Workflow

```text
.tmn Source Code
       │
       ▼
Lexical Analysis
       │
       ▼
Tokens
       │
       ▼
Syntax Analysis
       │
       ▼
Abstract Syntax Tree
       │
       ▼
Python Code Generation
       │
       ▼
Arduino / Firmata Execution
```

The compiler receives source code with:

```python
Comp.compile(code)
```

It tokenizes the code, generates an abstract syntax tree, and produces executable Python instructions.

---

## 🎛️ Available Hardware Commands

### 🥁 Percutor

Controls a percussion position:

```text
Percutor(D, 1)
Percutor(I, 1)
Percutor(A, 1)
Percutor(B, 1)
Percutor(DI, 1)
Percutor(AB, 1)
```

Possible positions include:

- `D` — Right
- `I` — Left
- `A`
- `B`
- `DI` — Right/Left combination
- `AB` — Combined movement

### 💥 Golpe

Activates the strike mechanism:

```text
Golpe(1)
```

### 🔄 Vibrato

Repeats a servo movement:

```text
Vibrato(10, 1)
```

### ↕️ Vertical

Moves the instrument vertically:

```text
Vertical(D, 1)
Vertical(I, 1)
```

### 🌬️ Abanico

Defines left or right fan movement:

```text
Abanico(A, 1)
Abanico(B, 1)
```

### ⏱️ Metronomo

Controls metronome timing:

```text
Metronomo(A, 1)
Metronomo(D, 1)
```

- `A` — Activate
- `D` — Deactivate

---

## ✅ Requirements

- 🐍 Python 3
- 📦 `pyfirmata`
- 🖼️ Tkinter
- 🔧 An Arduino board
- 🔌 A USB COM/serial connection
- ⚙️ Servo motors and motors for the physical device
- 💡 LED for visual timing
- 🪘 The assembled Arduino-controlled tambourine

---

## ⬇️ Installation

Clone the repository:

```bash
git clone https://github.com/Isaacoun100/Tambarduine.git
cd Tambarduine
```

Install PyFirmata:

```bash
pip install pyfirmata
```

Tkinter is often included with Python, but it may require a separate package on Linux distributions.

---

## ▶️ Running the IDE

Run the main entry point:

```bash
python main.py
```

The IDE opens in fullscreen mode and provides options to:

- Open `.tmn` files
- Edit source code
- Save files
- Compile code
- Compile and run code
- Navigate to a specific line

The IDE has keyboard support for:

- `F5` — Compile
- `Esc` — Exit fullscreen or close the IDE

---

## 📂 Tambarduine File Format

Tambarduine programs use the `.tmn` extension.

Example files are located in:

```text
Prueba/
```

Example categories include:

- `Percutor(...).tmn`
- `Vibrato().tmn`
- `Golpe().tmn`
- `Vertical(...).tmn`
- `Metronomo(...).tmn`
- `Abanico(...).tmn`

---

## 🧪 Running Tests

Run the test suite:

```bash
python -m unittest discover tests
```

or:

```bash
pytest
```

depending on the testing tools installed.

---

## 🔌 Arduino Configuration

The hardware instructions currently use the following Arduino port:

```python
pyfirmata.Arduino('COM3')
```

On Windows, `COM3` may need to be changed to match the Arduino's assigned serial port.

Example pins include:

| Pin | Purpose |
|---|---|
| 2–10 | Motor and servo direction control |
| 10 | Servo control |
| 11 | Status LED |
| 12–13 | Strike mechanism |
| 3–9 | Tambourine movement motors |

---

## ⚠️ Hardware and Safety Notes

- 🔌 Disconnect power before changing connections
- 🔧 Verify pin assignments before running a routine
- ⚡ Do not exceed the Arduino or motor voltage ratings
- 🔋 Use an appropriate external power supply
- 🪛 Secure the tambourine mechanism before testing
- 🧪 Start with low motor speeds or short routines
- 🛑 Stop execution if the motors behave unexpectedly
- 🖥️ Update `COM3` to match the actual serial port

---

## 🔮 Future Improvements

- 🔌 Cross-platform Arduino port selection
- 🛑 Stop-running button
- ⏱️ Improved metronome implementation
- 🧩 Extended language syntax
- 🧠 Better semantic analysis
- ⚠️ More descriptive compiler errors
- 🎨 Syntax highlighting
- 💾 Autosave support
- 📤 Export compiled routines
- 🧪 Automated hardware tests
- 🔧 Motor calibration controls
- 🐳 Virtual hardware simulation
- 📚 Complete language specification
- 📜 Add a project license
- 🎵 Predefined rhythm library
- 🎛️ Improved servo position control
- 🧭 Improved handling of Arduino disconnections

---

## 📌 Repository Information

- **Repository:** [Isaacoun100/Tambarduine](https://github.com/Isaacoun100/Tambarduine)
- **Language:** Python — 100%
- **Default branch:** `main`
- **Hardware:** Arduino
- **IDE:** Tkinter
- **Compiler source format:** `.tmn`
- **License:** No license specified
- **Project type:** Custom language and physical computing project

---

## 👤 Authors

- [Isaac Herrera Monge](https://github.com/Isaacoun100)
- [Eduardo Zumbado Granados](https://github.com/Eduardo2108)
- [Jose Espinoza](https://github.com/JoseA4718)
