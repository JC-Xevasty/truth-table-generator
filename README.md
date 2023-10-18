# Truth Table Generator using Python

## [Demo (CodeSandbox)](https://codesandbox.io/p/sandbox/proposition-truth-table-msv279)

Generate a **truth table** based from a logical expression with up to 5 propositions.

These are the possible operators that can be used to form a logical expression

|  OPERATORS  | KEYWORDS     |
|-------------|--------------|
| Negation    | `not`        |
| Conjunction | `and`        |
| Disjunction | `or`         |
| Implication | `implies`    |
| True        | `T` / `True` |
| False       | `F` / `False`|

Propositions can be an uppercase letter except for `T` and `F`.

Correct pairing of **parentheses** must be observed. 

Some examples of logical expression:

* `A and B`
* `C implies D or not E`
* `(not (F and G) implies (H or I)) and J`
* `K or True and (False implies L)`

These logical expression will not be accepted:

* `A and B and C and D and E and F`
> Six propositions were used in the expression
* `((A and B) and C or D`
> The expression is missing a closing parentheses

Here is a sample output based on the expression **`A and B`**

```
╔═════════════════════════════╗  
║         TRUTH TABLE         ║  
╠═════════════════════════════╣  
║ │   A   │   B   │  A and B  ║  
╠═════════════════════════════╣  
║ │ False │ False │   False   ║  
║ │ False │ True  │   False   ║  
║ │ True  │ False │   False   ║  
║ │ True  │ True  │   True    ║  
╚═════════════════════════════╝ 
```






