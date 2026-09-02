# ⚙️ JCL PROC Resolver — Mainframe Automation

<p align="center">
  <strong>Automating JCL fragment aggregation and PROC resolution for mainframe workflows.</strong>
</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-Automation-blue?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/Mainframe-JCL-orange?style=for-the-badge" />
<img src="https://img.shields.io/badge/NatWest-Internship-purple?style=for-the-badge" />

</p>

---

## 🧭 Overview

Mainframe applications often contain large **JCL (Job Control Language)** workflows where job steps, procedures and definitions are distributed across multiple files and directories.

When these files are inspected individually, understanding the **actual execution flow** can become difficult and time-consuming.

This project explores a Python-based approach to:

* 📂 Discover and collect JCL fragments
* 🔗 Combine related file fragments
* 🧩 Identify and work with `PROC` definitions
* 🔍 Resolve procedure references
* 📝 Generate consolidated output
* 🧪 Validate the resulting structure
* 📊 Improve traceability between source and processed files

### The core idea

```text
        Fragmented JCL
        + PROC Definitions
                │
                ▼
       ┌──────────────────┐
       │ File Discovery    │
       │ & Collection      │
       └────────┬─────────┘
                │
                ▼
       ┌──────────────────┐
       │ Fragment Merging  │
       │ & Processing      │
       └────────┬─────────┘
                │
                ▼
       ┌──────────────────┐
       │ PROC Resolution   │
       │ & JCL Analysis    │
       └────────┬─────────┘
                │
                ▼
       ┌──────────────────┐
       │ Resolved Output   │
       │ & Traceability    │
       └──────────────────┘
```

---

# 🎯 Problem Statement

A JCL job may reference procedures that are defined somewhere else.

For example:

```jcl
//MYJOB    JOB ...
//STEP01   EXEC PROC=MYPROC
```

The actual procedure may exist in a separate file:

```jcl
//MYPROC   PROC
//STEP01   EXEC PGM=PROGRAM1
//STEP02   EXEC PGM=PROGRAM2
//MYPROC   PEND
```

Manually tracing these relationships across multiple files can become cumbersome.

The purpose of this project is to automate that process and transform fragmented source material into a **more understandable representation of the JCL structure**.

---

# 🚀 What the Project Does

The workflow focuses on four main stages.

### 1. 📂 Collect

Locate JCL fragments distributed across multiple directories.

```text
folder1/
├── fragment_A
├── fragment_B
└── fragment_C

folder2/
├── fragment_D
└── fragment_E
```

### 2. 🔍 Identify

Inspect the available JCL content and identify relevant components such as:

```text
JCL
│
├── JOB
├── EXEC
├── PROC
└── DD
```

### 3. 🔗 Merge

Combine related fragments into a consolidated representation.

```text
Fragment A ─────┐
Fragment B ─────┼──────► Combined JCL
Fragment C ─────┘
```

The repository includes `merge_files.py` as part of this processing workflow.

### 4. 🧩 Resolve

Trace procedure references and connect them with their corresponding definitions.

```text
JOB
│
├── EXEC PROC_A
│      │
│      ├── STEP01
│      ├── STEP02
│      └── STEP03
│
└── EXEC PROC_B
       │
       ├── STEP04
       └── STEP05
```

The result is a structure that is easier to inspect and reason about.

---

# 🧠 Why PROC Resolution?

JCL frequently separates **job invocation** from **procedure implementation**.

A job may contain:

```jcl
//STEP01 EXEC PROC=PAYPROC
```

while the implementation is stored elsewhere:

```jcl
//PAYPROC  PROC
//PAYSTEP1 EXEC PGM=PAYMENT
//PAYSTEP2 EXEC PGM=VALIDATE
//PAYPROC  PEND
```

A PROC resolver bridges this gap:

```text
EXEC PROC=PAYPROC
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
 Generate structure
```

This helps transform **references into relationships** and isolated files into a more complete execution picture.

---

# 🏗️ Repository Structure

```text
JCL-PROC-Resolver_Script_Natwest_Internship/
│
├── 📁 folder1/
│   ├── PCJE1D1W.txt
│   ├── PCJUB2CW.txt
│   ├── PCNE1D1W.txt
│   ├── PCNE1D2W.txt
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
│   └── PCNUB2CW.txt
│
├── 🖼️ File_Fragment_1_Folder1.png
├── 🖼️ File_Fragment_2_Folder2.png
├── 🖼️ Result_Fragment1 + Fragment2.png
├── 🖼️ Terminal_Action_Overflow.png
│
└── 📄 README.md
```

The repository contains sample JCL fragments, processing scripts and visual evidence demonstrating the workflow.

---

# 🔬 Example

### Input JCL

```jcl
//JOB001   JOB ...
//STEP01   EXEC PROC=PAYPROC
```

### PROC Definition

```jcl
//PAYPROC  PROC
//PAYSTEP1 EXEC PGM=PAYMENT
//PAYSTEP2 EXEC PGM=VALIDATE
//PAYPROC  PEND
```

### Resolved Representation

```text
JOB001
│
└── STEP01
     │
     └── PAYPROC
          ├── PAYSTEP1 → PAYMENT
          └── PAYSTEP2 → VALIDATE
```

Instead of manually navigating between the job and its procedure definition, the relationship becomes immediately visible.

---

# 📊 Before vs After

### BEFORE — Fragmented

```text
📄 File A
└── JCL fragment

📄 File B
└── PROC definition

📄 File C
└── Additional steps

📄 File D
└── Related definition
```

⬇️

### AFTER — Resolved

```text
┌─────────────────────────────────────┐
│           RESOLVED JCL FLOW         │
├─────────────────────────────────────┤
│ JOB                                 │
│  │                                  │
│  ├── PROC A                         │
│  │    ├── STEP 01                  │
│  │    └── STEP 02                  │
│  │                                  │
│  └── PROC B                         │
│       ├── STEP 03                  │
│       └── STEP 04                  │
└─────────────────────────────────────┘
```

---

# 🛠️ Technology Stack

| Technology             | Purpose                                |
| ---------------------- | -------------------------------------- |
| 🐍 **Python**          | Automation and file processing         |
| 🖥️ **JCL**            | Mainframe job-control language         |
| 📄 **TXT**             | JCL and PROC source fragments          |
| 🔗 **File Processing** | Fragment aggregation and manipulation  |
| 🐙 **Git / GitHub**    | Version control and project management |

---

# 🎯 Project Objectives

The project was developed around several practical engineering objectives.

### 01 — Reduce Manual Inspection

Automate repetitive navigation and processing of JCL fragments.

### 02 — Improve Traceability

Maintain a clear connection between source fragments and generated output.

### 03 — Simplify Legacy-System Analysis

Make relationships between jobs, procedures and execution steps easier to understand.

### 04 — Explore Automation Opportunities

Apply Python scripting to a workflow involving established enterprise/mainframe technologies.

---

# 📸 Project Evidence

The repository includes screenshots demonstrating different stages of the workflow:

### 📂 Source Fragments

Examples of JCL fragments distributed across separate directories.

### 🔗 Combined Output

Evidence of the fragments being processed into a consolidated representation.

### 🖥️ Terminal Execution

Screenshots documenting the execution of the processing workflow.

These artifacts provide visual context for how the input files are transformed during processing.

---

# 🧪 Validation

The workflow can be validated by comparing:

```text
Source Fragments
       │
       ▼
   Processing
       │
       ▼
Resolved Output
       │
       ▼
Structural Validation
```

The objective is to ensure that relevant JCL and PROC relationships are preserved during processing.

---

# 💡 Engineering Learnings

This project provided practical exposure to the intersection of:

```text
Python Automation
        ×
Mainframe Technology
        ×
Legacy Code Analysis
```

Key areas explored include:

* JCL structure and syntax
* `PROC` definitions and references
* File parsing and manipulation
* Fragment aggregation
* Automation of repetitive workflows
* Input/output validation
* Debugging
* Terminal-based execution
* Working with legacy-oriented enterprise systems

---

# 🔮 Future Improvements

The current workflow could be extended with:

* [ ] 🔍 Automated PROC dependency graphs
* [ ] 🌳 Visual JCL execution trees
* [ ] 📊 Structured JSON output
* [ ] ⚡ Parallel processing for larger repositories
* [ ] 🧪 Automated unit and integration tests
* [ ] 🖥️ Web-based JCL visualization
* [ ] 🚨 Improved unresolved-PROC error reporting
* [ ] 📈 Processing and performance metrics
* [ ] 🔄 CI/CD integration
* [ ] 📚 Automated documentation generation

---

# 🏦 Internship Context

This project was developed during my **NatWest internship**, providing practical experience with enterprise technologies and mainframe-oriented workflows.

The project explores how modern scripting and automation techniques can be applied to improve the analysis and processing of existing enterprise systems.

---

# 👨‍💻 Author

<p align="center">

<strong>Rutvik Barbhai</strong>

<br><br>

<a href="https://github.com/rutvikbarbhai">
  <img src="https://img.shields.io/badge/GitHub-rutvikbarbhai-black?style=for-the-badge&logo=github" />
</a>

</p>

---

# ⭐ Final Thought

> **Turn references into relationships.**
> **Turn fragments into structure.**
> **Turn complexity into clarity.**

<p align="center">

### ⚙️ JCL In → 🔍 Resolve → 🧩 Structure Out

<strong>Built with Python • JCL • Automation • Curiosity</strong>

</p>
