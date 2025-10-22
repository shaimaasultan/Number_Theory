# ShoSho Sequence Generator

## 🧐 Overview

This repository contains a Python script that generates a unique sequence of tuples, **(i, k)**, where $i$ is an odd number and $k$ is a specific count derived from trial division. The resulting list $L$ contains a pair for every odd number in the given range.

The algorithm exhibits a fascinating and consistent pattern for **prime numbers**, where the counter $k$ is related to the prime $P$ by the formula **$k = (P-1)/2$**.

***

## 🛠️ Usage

### Prerequisites

* Python 3.x

### Running the Script

1.  Clone this repository:
    ```bash
    git clone (https://github.com/shaimaasultan/Number_Theory)
    cd Number_Theory
    ```
2.  Run the function with a specified `limit`:

    ```python
    # Example usage in a Python environment or script
    from Number_Theory import ShoSho  # Assuming your file is named Number_Theory.py
    limit = 40
    results = ShoSho(limit)
    print(results)
    ```

***

## 💻 The Algorithm (`ShoSho(limit)`)

The core of the project is the `ShoSho` function, which performs a modified trial division and list update.

### 1. List Content (The $i$ value)

The list $L$ is initialized with **(2, 1)** and then guaranteed to include a pair for **every odd number** $i$ checked by the loop (from 3 up to $\text{limit}-2$).

### 2. The Counter ($k$ value)

The value $k$ in the tuple $(i, k)$ represents the **total number of divisibility checks performed** before the inner loop terminates.

| Number Type ($i$) | Condition | Final $k$ Value |
| :---: | :---: | :--- |
| **Prime ($P$)** | Loop completes (no divisor found). | The number of elements in $L$ checked against $P$. This consistently matches: $$k = \frac{P - 1}{2}$$ |
| **Composite ($C$)** | Loop terminates early (divisor found). | A small integer (often **1 or 2**) corresponding to the position of $C$'s smallest prime factor in the divisor list $L$ when the check broke. |

***

## 💡 Observed Prime Pattern

For prime numbers $P$, the counter $k$ follows a highly regular arithmetic progression:

| Prime ($P$) | $k$ Value (Checks) | $(P-1)/2$ |
| :---: | :---: | :---: |
| 11 | 5 | 5 |
| 13 | 6 | 6 |
| 17 | 8 | 8 |
| 19 | 9 | 9 |

This pattern highlights an explicit, deterministic link between the magnitude of the prime number and the computational effort ($k$) required to verify its primality within this unique algorithm.

***

## 🤝 Contribution

Feel free to open issues or submit pull requests if you have suggestions for optimization or further analysis of the generated sequence.

## Verfied using Gemini

<img src="/image/Screenshot 2025-10-21 214848.png" />
<img src="/image/Screenshot 2025-10-21 215304.png" />
<img src ="/image/Screenshot 2025-10-21 215315.png"/>
<img src="/image/Screenshot 2025-10-21 215419.png" />
<img src="/image/Screenshot 2025-10-21 215430.png" />
<img src="/image/Screenshot 2025-10-21 165901.png" />

***

## 📄 License

This project is open-source. (Insert License Here)
