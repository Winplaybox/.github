---
name: diagnosing-bugs
description: Disciplined diagnosis loop for hard bugs and performance regressions. Use when the user says diagnose or debug this, or reports something broken, throwing, failing, or slow.
---

<!-- Adapted from mattpocock/skills (diagnosing-bugs), MIT License, Copyright (c) 2026 WinPlayBox

# Diagnosing Bugs

A discipline for hard bugs. Skip phases only when explicitly justified. Read `GLOSSARY.md` (if it exists) and ADRs in the area first.

## Redact

Redact every secret in commands, outputs and artifacts you show (`<REDACTED>`). Keep credentials in env vars. Quote only the lines that carry the signal. If redacted output isn't enough, say so and ask the user.

## Phase 1: Build a feedback loop

**This is the skill.** With a tight pass/fail signal that goes red on _this_ bug, you will find the cause. Without one, staring at code won't save you. Be aggressive and creative here.

Ways to build one, roughly in order:
1. Failing test at whatever seam reaches the bug (unit, integration, e2e).
2. Curl / HTTP script against a running dev server.
3. CLI invocation with fixture input, diffed against a known-good snapshot.
4. Headless browser script (Playwright/Puppeteer) asserting on DOM/console/network.
5. Replay a captured trace (request, payload, event log) through the code path.
6. Throwaway harness: minimal subset of the system with mocked deps.
7. Property/fuzz loop for "sometimes wrong" bugs.
8. Bisection harness + `git bisect run` when the bug appeared between two known states.
9. Differential loop: same input through old vs new version, diff outputs.
10. Last resort: a structured human-in-the-loop script that tells the user exactly what to click and captures their observations.

**Tighten the loop**: faster (cache setup, narrow scope), sharper (assert the specific symptom, not "didn't crash"), deterministic (pin time, seed RNG, freeze network). A 2-second deterministic loop beats a 30-second flaky one.

**Non-deterministic bugs**: aim for a higher reproduction rate — loop 100×, parallelise, add stress, inject sleeps — until it's debuggable.

**Can't build a loop?** Stop and say so, list what you tried, and ask for environment access, a redacted artifact (HAR, logs, recording), or permission for temporary instrumentation. Don't hypothesise without a loop.

**Done when** you can name one command you have already run (show it, redacted) that is red-capable (asserts the user's exact symptom), deterministic, fast, and runnable without a human. If you catch yourself theorising before this exists, stop.

## Phase 2: Reproduce + minimise

Run the loop and confirm it shows the **user's** failure, not a nearby one, reproducibly, with the exact symptom captured. Then shrink: cut inputs, callers, config, steps one at a time, re-running each time, until every remaining element is load-bearing.

## Phase 3: Hypothesise

Generate **3–5 ranked, falsifiable hypotheses** before testing any: "If <X> is the cause, then changing <Y> makes the bug disappear / changing <Z> makes it worse." No prediction = discard. Show the ranked list to the user (they may re-rank instantly); don't block if they're away.

## Phase 4: Instrument

Each probe maps to one prediction; change one variable at a time. Prefer debugger/REPL, then targeted logs at boundaries that distinguish hypotheses. Never log everything and grep. Tag debug logs with a unique prefix like `[DEBUG-a4f2]`. For perf regressions: baseline measurement first (timer, profiler, query plan), then bisect.

## Phase 5: Fix + regression test

Write the regression test before the fix, but only at a **correct seam** — one that exercises the real bug pattern as it occurs. If none exists, that is a finding: note that the architecture prevents locking the bug down.

With a seam: turn the minimised repro into a failing test, watch it fail, fix, watch it pass, then re-run the original Phase 1 loop.

## Phase 6: Cleanup

- [ ] Original repro no longer reproduces
- [ ] Regression test passes (or missing seam documented)
- [ ] All `[DEBUG-...]` logs removed (grep the prefix)
- [ ] Throwaway prototypes deleted
- [ ] Correct hypothesis stated in the commit/PR message
