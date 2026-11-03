# Contributing to Terrible Libraries

Thank you for your interest in making the world a slightly worse place.

## Guidelines

1. **It must work** (for some reasonable set of inputs).  
   Returning the wrong answer for everything is too easy. We want functions that *almost* work.

2. **It must be terrible**.  
   If a normal developer looks at your code and says "that's fine", you have failed.

3. **Prefer these techniques:**
   - Giant chains of `if` / `elif` / `switch` / `match`
   - Hardcoded lookup tables
   - Unnecessary recursion
   - Converting numbers to strings (and back)
   - Sleeping / busy-waiting
   - Allocating way more memory than needed
   - Using reflection / eval / dynamic features when static would be better
   - Copy-pasting the same logic many times instead of using a loop

4. **Do not** use the correct algorithm unless you have thoroughly sabotaged it.

5. Each language should live in its own folder.
6. Each function should preferably be in its own file (or clearly separated).
7. Add a short comment at the top explaining *why* it's terrible (optional but appreciated).

## Adding a New Language

1. Create a new folder named after the language (lowercase).
2. Implement at least `is_even` in the spirit of the existing ones.
3. Update the README language table.

## Adding a New Function

1. Implement it in as many languages as you can.
2. Keep the interface simple and consistent across languages where possible.
3. Document any particularly cursed decisions.

## Pull Request Title Format

```
Add terrible <function> in <language>
```

or

```
Make <function> even worse in <language>
```

We reserve the right to reject contributions that are too reasonable.
