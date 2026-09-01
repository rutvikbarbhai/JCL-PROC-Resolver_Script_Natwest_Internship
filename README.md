# ⚙️ JCL PROC Resolver For Main Frame Computers Automation 



---

## 🧭 The Problem

Mainframe workloads can contain large JCL flows where procedures, job steps and definitions are distributed across multiple files.

When these fragments are viewed independently, understanding the **actual execution structure** can become difficult.

This project approaches the problem as a simple pipeline:

```text
                 ┌──────────────────────┐
                 │   Fragmented JCL      │
                 │   + PROC definitions  │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   File Discovery     │
                 │   & Collection       │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Merge / Processing  │
                 │       Logic          │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    PROC Resolver     │
                 │   & JCL Structure    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │  Resolved Output     │
                 │  + Traceability      │
                 └──────────────────────┘
```

The goal is to turn a collection of difficult-to-follow fragments into something that is easier to **inspect, understand and validate**.

---

# 🚀 What This Project Does

The repository demonstrates a workflow for handling JCL fragments and PROC-related definitions.

### Core capabilities

* 📂 Process JCL fragments stored across multiple directories
* 🔗 Combine related file fragments
* 🧩 Work with JCL `PROC` / procedure definitions
* 🔍 Resolve relationships between JCL components
* 📝 Generate processed output for inspection
* 🧪 Support validation through example inputs and outputs
* 🖥️ Provide visual evidence of the processing workflow

---

# 🏗️ Repository Architecture

```text
JCL-PROC-Resolver_Script_Natwest_Internship/
│
├── 📁 folder1/
│   ├── PCJE1D1W.txt
│   ├── PCJUB2CW.txt
│   ├── PCNE1D1W.txt
│   ├── PCNE1D2W.txt
│   ├── ...
│   └── merge_files.py
│
├── 📁 folder2/
│   ├── PC#E1D1W.txt
│   └── PCUB02CD.txt
│
├── 📁 folder3/
│   ├── PCJE1D1W.txt
│   ├── PCJUB2CW.txt
│   ├── PCNE1D1W.txt
│   ├── PCNE1D2W.txt
│   ├── ...
│   └── PCNUB2CW.txt
│
├── 🖼️ File_Fragment_1_Folder1.png
├── 🖼️ File_Fragment_2_Folder2.png
├── 🖼️ Result_Fragment1 + Fragment2.png
├── 🖼️ Terminal_Action_Overflow.png
│
└── 📄 README.md
```

The repository currently contains three primary input folders, sample JCL text files, a Python merge script and screenshots documenting the processing/output flow.

---

# 🔬 How It Works

## 1️⃣ Collect

The resolver starts with JCL fragments distributed across the input directories.

```text
folder1/
 ├── fragment A
 ├── fragment B
 └── fragment C

folder2/
 ├── fragment D
 └── fragment E
```

---

## 2️⃣ Identify

The processing logic examines the available JCL content and identifies the relevant procedure and job-definition fragments.

```text
JCL
 │
 ├── JOB
 │
 ├── EXEC
 │
 ├── PROC
 │
 └── DD
```

---

## 3️⃣ Merge

Related fragments can be brought together into a consolidated representation.

```text
Fragment A ─────┐
                │
Fragment B ─────┼──────► Combined JCL
                │
Fragment C ─────┘
```

The repository includes `merge_files.py` as part of this workflow.

---

## 4️⃣ Resolve

The important step is moving from isolated definitions to a more complete representation of the JCL/PROC relationship.

```text
JOB
 │
 ├── EXEC PROC_A
 │       │
 │       ├── STEP01
 │       ├── STEP02
 │       └── STEP03
 │
 └── EXEC PROC_B
         │
         ├── STEP04
         └── STEP05
```

This makes complex procedure-driven JCL easier to reason about.

---

# 🧠 Why PROC Resolution Matters

A JCL job can reference procedures rather than explicitly containing every execution statement.

Conceptually:

```jcl
//MYJOB    JOB ...
//STEP01   EXEC PROC=MYPROC
```

The actual logic may live elsewhere:

```jcl
//MYPROC   PROC
//STEP01   EXEC PGM=PROGRAM1
//STEP02   EXEC PGM=PROGRAM2
//MYPROC   PEND
```

A resolver bridges the gap:

```text
EXEC PROC=MYPROC
        │
        ▼
   Locate PROC
        │
        ▼
   Read definition
        │
        ▼
   Resolve steps
        │
        ▼
   Produce usable structure
```

---

# 🛠️ Technology Stack

| Technology             | Purpose                                        |
| ---------------------- | ---------------------------------------------- |
| 🐍 **Python**          | Automation and processing                      |
| 🖥️ **JCL**            | Mainframe job-control language being processed |
| 📄 **TXT files**       | JCL / PROC input fragments                     |
| 🧩 **File Processing** | Combining and manipulating fragments           |
| 🐙 **Git / GitHub**    | Version control and project collaboration      |

---

# 📸 Project Evidence

### Input Fragment — Folder 1

The repository includes an example screenshot showing one of the source fragments.

### Input Fragment — Folder 2

A second fragment demonstrates how the source material can be distributed across different locations.

### Resolved / Combined Result

The resulting screenshot demonstrates the output after processing the fragments.

### Terminal Execution

A terminal screenshot documents the execution workflow.

> These artifacts are intentionally included in the repository to make the transformation process easier to understand visually.

---

# 🎯 Project Objectives

The project was designed around several practical engineering goals:

### 01 — Reduce manual inspection

Instead of manually navigating through multiple JCL fragments, automate the collection and processing workflow.

### 02 — Improve traceability

Maintain a clear relationship between source fragments and processed output.

### 03 — Simplify legacy-system analysis

Make complex JCL/PROC relationships easier for engineers to inspect.

### 04 — Build reusable automation

Use Python to automate repetitive mainframe-development tasks.

---

# 📊 Conceptual Transformation

```text
BEFORE
────────────────────────────────────────────

📄 File A
   └── JCL fragment

📄 File B
   └── PROC definition

📄 File C
   └── Additional steps

📄 File D
   └── Related definition


                    ↓
              🔧 RESOLVER
                    ↓


AFTER
────────────────────────────────────────────

┌─────────────────────────────────────────┐
│              RESOLVED FLOW               │
├─────────────────────────────────────────┤
│ JOB                                      │
│   ├── PROC A                             │
│   │    ├── STEP 01                       │
│   │    └── STEP 02                       │
│   │                                      │
│   └── PROC B                             │
│        ├── STEP 03                       │
│        └── STEP 04                       │
└─────────────────────────────────────────┘
```

---

# 💡 Engineering Takeaways

This project provided hands-on exposure to an interesting intersection of:

**Python Automation × Mainframe Technology × Legacy Code Analysis**

Key areas explored include:

* JCL structure and syntax
* PROC-based execution
* File parsing
* Fragment aggregation
* Automation of repetitive workflows
* Input/output validation
* Debugging and terminal-based execution
* Working with legacy-oriented enterprise systems

---

# 🔮 Future Improvements

Potential extensions could include:

* [ ] 🔍 Automated PROC dependency graph generation
* [ ] 🌳 Visual JCL execution-tree generation
* [ ] 📊 Structured JSON output
* [ ] ⚡ Parallel processing for large JCL repositories
* [ ] 🧪 Automated unit and integration tests
* [ ] 🖥️ Web-based JCL visualisation
* [ ] 🚨 Better error reporting for unresolved PROCs
* [ ] 📈 Processing and performance metrics
* [ ] 🔄 CI/CD integration
* [ ] 📚 Automated documentation generation

---

# 🧪 Example Concept

Given:

```jcl
//JOB001   JOB ...
//STEP01   EXEC PROC=PAYPROC
```

and a PROC definition:

```jcl
//PAYPROC  PROC
//PAYSTEP1 EXEC PGM=PAYMENT
//PAYSTEP2 EXEC PGM=VALIDATE
//PAYPROC  PEND
```

the conceptual resolved representation becomes:

```text
JOB001
 │
 └── STEP01
      │
      └── PAYPROC
           ├── PAYSTEP1 → PAYMENT
           └── PAYSTEP2 → VALIDATE
```

That is the central idea behind a **JCL PROC Resolver**:

> **Turn references into relationships.
> Turn fragments into structure.
> Turn complexity into clarity.**

---

# 🏦 Internship Context

This project was developed as part of my **NatWest internship experience**, with a focus on understanding and automating workflows involving enterprise/mainframe technologies.

It represents practical exploration of how modern scripting and automation techniques can be applied to existing enterprise systems.

---

# 👨‍💻 Author

### Rutvik Barbhai

<p align="center">

<a href="https://github.com/rutvikbarbhai">
  <img src="https://img.shields.io/badge/GitHub-rutvikbarbhai-black?style=for-the-badge&logo=github" />
</a>

</p>

---

# ⭐ If You Found This Interesting

Feel free to explore the repository, inspect the JCL fragments, follow the processing workflow and experiment with the resolver.

<p align="center">

### ⚙️ JCL in → 🔍 Resolution → 🧩 Structure out

**Built to make legacy complexity easier to understand.**

</p>

---

<p align="center">
  <sub>Built with Python • JCL • Curiosity • Automation</sub>
</p>
