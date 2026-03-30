---
title: "Getting Started"
---

# Getting Started

This course uses **Jupyter Book** with live, executable notebooks. This means the pages are not just static text — you can run code, move sliders, change parameters, and see results update instantly, all inside your browser.
```{admonition} No installation required
:class: tip
Everything runs in the cloud. You do not need to install Python or any library on your computer.
```

---

## How Executable Pages Work

Some pages in this book contain **live code cells** — blocks of Python code that you can execute directly. These cells power the interactive widgets and figures you will encounter throughout the course.

Under the hood, each page is a Jupyter notebook running on a remote server. When you activate it, a **Python kernel** starts, loads all the necessary libraries, and stands by to run your code.

---

## Step-by-Step: Your First Interactive Page

### 1 — Launch the kernel

At the top of any executable page, click the 🚀 **rocket icon** in the top toolbar, then select **Live Code** (or **Binder** / **JupyterHub**, depending on your setup).
```{figure} ../assets/images/launch_button.png
:width: 60%
:align: center
:alt: Screenshot of the launch button in Jupyter Book
Click the rocket icon to activate live code on the page.
```

You will see a status message while the kernel starts — this can take **20–30 seconds** the first time. Once the kernel is ready, all code cells become interactive.

---

### 2 — Run a cell

Each code cell has a **Run** button on the left, or you can click inside the cell and press:

> **`Shift + Enter`** — run the current cell and move to the next  
> **`Ctrl + Enter`** — run the current cell and stay on it

The output (text, plot, or widget) appears directly below the cell.
```{admonition} Nothing happening?
:class: caution
If a cell does not respond, the kernel may still be loading. Wait for the status indicator to show **idle** (a small circle in the toolbar), then try again. If the problem persists, restart the kernel via the toolbar menu.
```

---

### 3 — Use widgets and sliders

Many pages include **interactive widgets**: sliders, dropdowns, and input boxes that let you change parameters without editing any code. Just:

- **Drag a slider** to change a value continuously
- **Select from a dropdown** to switch between scenarios
- **Type a value** into a number box for precise input

The output updates automatically — no need to press anything extra.
```{figure} ../assets/images/widget_example.png
:width: 70%
:align: center
:alt: Example of an interactive slider widget
Example widget: drag the slider and watch the plot update in real time.
```

---

### 4 — Observe and interpret the results

Widgets are not just animations — they are learning tools. As you change parameters, ask yourself:

- What happens to the output when I increase this value?
- Does the result match my physical intuition?
- At what threshold does the behaviour change?

This kind of exploration is the core of the practical sections of this course.

---

## Exporting the Book to PDF
```{tip}
To save a page as a PDF, click the **download icon** (⬇) in the top toolbar and select **PDF**. 

For the best result:
- Make sure all cells have been executed first so outputs are visible in the export
- Use your browser's **Print → Save as PDF** option if the toolbar button is unavailable
- Note that interactive widgets will appear as static images in the PDF — they are only live in the browser
```

---

## Tips for Success
```{tip}
- **Activate the kernel before anything else** — widgets will not respond until the kernel is running
- **Complete sections in order** — each notebook builds on concepts introduced in the previous one
- **Try exercises before looking at solutions** — the struggle is where the learning happens
- **Play with the widgets** — changing parameters and observing effects is as important as reading the theory
- **Ask questions** — use the course discussion forum if something does not behave as expected
```