# Terrible Libraries

> Functions that work.  
> Functions that are correct for the cases you actually test.  
> Functions that make experienced developers question their career choices.

This repository contains intentionally terrible implementations of common functions across many programming languages. Every function is designed to be:

- Correct (for a limited and convenient set of inputs)
- Painfully inefficient
- Hardcoded where possible
- Full of anti-patterns
- A crime against computer science

## Philosophy

We believe that the best way to appreciate good code is to suffer through truly awful code.  
These libraries are educational in the same way that a car crash is educational.

**Rules of the road:**
- Prefer giant `if` / `switch` chains over math
- Prefer recursion over loops (and vice-versa when it hurts more)
- Prefer string conversions and parsing over direct operations
- Prefer looking things up in massive tables over calculating them
- Never use the obvious solution if a worse one exists
- Sleeping, printing debug info, and allocating unnecessary memory are encouraged

## Available Functions

| Function          | Description                                      | Status      |
|-------------------|--------------------------------------------------|-------------|
| `is_even`         | Determines if a number is even                   | ✅ Terrible |
| `is_odd`          | Determines if a number is odd                    | ✅ Terrible |
| `is_prime`        | Checks if a number is prime                      | ✅ Terrible |
| `add`             | Adds two numbers                                 | ✅ Terrible |
| `subtract`        | Subtracts two numbers                            | ✅ Terrible |
| `multiply`        | Multiplies two numbers                           | ✅ Terrible |
| `max` / `min`     | Returns the larger / smaller of two values       | ✅ Terrible |
| `absolute`        | Returns the absolute value                       | ✅ Terrible |
| `factorial`       | Computes factorial (limited range)               | ✅ Terrible |
| `is_palindrome`   | Checks if a number/string is a palindrome        | ✅ Terrible |
| `strlen`          | Returns the length of a string                   | ✅ Terrible |
| `to_upper`        | Converts a string to uppercase                   | 🚧 Coming  |
| `fibonacci`       | Returns the nth Fibonacci number                 | 🚧 Coming  |

## Language Support

| Language     | Folder        | Notes                          |
|--------------|---------------|--------------------------------|
| Python       | `python/`     | The purest form of suffering   |
| JavaScript   | `javascript/` | Async versions encouraged      |
| C            | `c/`          | Manual memory management optional |
| C++          | `cpp/`        | Templates optional (and bad)   |
| Go           | `go/`         | Goroutines for simple math     |
| Rust         | `rust/`       | `unsafe` encouraged            |
| Java         | `java/`       | Enterprise-grade terribleness  |
| PHP          | `php/`        | Exactly as you'd expect        |
| Ruby         | `ruby/`       | Beautiful but wrong            |
| Bash         | `bash/`       | Pure chaos                     |
| C#           | `csharp/`     | Corporate suffering            |

## Example

```python
from terrible import is_even

print(is_even(2))    # True
print(is_even(3))    # False
print(is_even(69))   # True  (of course)
print(is_even(70))   # False (everything after 69 is odd, apparently)
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

We welcome new languages, new functions, and new depths of horror.

## License

This project is licensed under the **Do What The Fuck You Want To Public License** (WTFPL).  
See [LICENSE](LICENSE) for details.

---

*Made with love, spite, and a complete disregard for best practices.*
