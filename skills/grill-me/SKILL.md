---
name: grill-me
description: Grill the user relentlessly about a plan, design, or idea to find every loophole. Use when the user says grill me, stress-test this, or wants a plan challenged.
---

<!-- Adapted from mattpocock/skills (grill-me + grilling), MIT License, Copyright (c) 2026 WinPlayBox

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Format a round like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Word each question so "yes" accepts your recommended answer.

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Finding _facts_ is your job, never the user's. When a frontier question needs a fact you can look up yourself (files, connected tools, the web), look it up instead of asking. Ask the rest of the frontier meanwhile; only questions downstream of the lookup wait. The _decisions_ are the user's: put each to them and wait.

Match the user's language (Hinglish is fine).

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on the plan until the user confirms you have reached a shared understanding.
