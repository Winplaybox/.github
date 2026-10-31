---
name: tdd
description: Test-driven development with red-green loop and behavior-focused tests. Use when the user wants to build features or fix bugs test-first, mentions red-green-refactor, or wants integration tests.
---

<!-- Adapted from mattpocock/skills (tdd), MIT License, Copyright (c) 2026 Matt Pocock -->

# Test-Driven Development

TDD is the red → green loop. This skill makes that loop produce tests worth keeping: what a good test is, where tests go, the anti-patterns, and the rules of the loop. Consult every section before and during the loop, not after.

When exploring the codebase, read `GLOSSARY.md` (if it exists) so test names match the project's domain language, and respect ADRs in the area you're touching.

## What a good test is

Tests verify behavior through public interfaces, not implementation details. Code can change entirely; tests shouldn't. A good test reads like a specification: "user can checkout with valid cart" says exactly what capability exists, and survives refactors.

Good test characteristics: tests behavior callers care about, uses public API only, survives internal refactors, describes WHAT not HOW, one logical assertion per test.

```typescript
// GOOD: observable behavior
test("user can checkout with valid cart", async () => {
  const cart = createCart();
  cart.add(product);
  const result = await checkout(cart, paymentMethod);
  expect(result.status).toBe("confirmed");
});

// BAD: implementation detail
test("checkout calls paymentService.process", async () => {
  const mockPayment = jest.mock(paymentService);
  await checkout(cart, payment);
  expect(mockPayment.process).toHaveBeenCalledWith(cart.total);
});

// BAD: bypasses interface
test("createUser saves to database", async () => {
  await createUser({ name: "Alice" });
  const row = await db.query("SELECT * FROM users WHERE name = ?", ["Alice"]);
  expect(row).toBeDefined();
});

// GOOD: verifies through interface
test("createUser makes user retrievable", async () => {
  const user = await createUser({ name: "Alice" });
  expect((await getUser(user.id)).name).toBe("Alice");
});
```

## Seams: where tests go

A **seam** is the public boundary you test at. Tests live at seams, never against internals.

**Test only at pre-agreed seams.** Before writing any test, list the seams under test and confirm them with the user, each with a one-line note on what it catches and what it misses. No test at an unconfirmed seam.

## When to mock

Mock at **system boundaries** only: external APIs (payment, email), databases (prefer a test DB), time/randomness, sometimes the file system. Never mock your own modules or internal collaborators.

Design boundaries for mockability: inject dependencies (`processPayment(order, paymentClient)` rather than constructing the client inside), and prefer SDK-style functions per operation (`api.getUser`, `api.createOrder`) over one generic `api.fetch(endpoint, options)`.

## Anti-patterns

- **Implementation-coupled**: mocks internal collaborators, tests private methods, or verifies through a side channel. Tell: breaks on refactor while behavior is unchanged.
- **Tautological**: expected value recomputed the way the code does (`expect(add(a, b)).toBe(a + b)`), so it passes by construction. Expected values must come from an independent source: a known literal, worked example, or the spec. E.g. `expect(calculateTotal([{price:10},{price:5}])).toBe(15)`.
- **Horizontal slicing**: all tests first, then all implementation. Work in **vertical slices**: one test → one implementation → repeat, each a tracer bullet informed by the last cycle.

## Rules of the loop

- **Red before green.** Write the failing test, run it, see it fail. Then only enough code to pass. No speculative features.
- **One slice at a time.** One seam, one test, one minimal implementation per cycle.
- **Refactoring is not part of the loop.** Do it at review time, not inside red → green.
