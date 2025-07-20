# string-compression-decompression

## Run-Length String Compression & Decompression

This Python project provides simple functions (and a class) to **compress** and **decompress** strings using run-length encoding.

- Compresses strings like `"aaabbcccc"` into `"3a2b4c"`
- Decompresses strings like `"3a2b4c"` back into `"aaabbcccc"`
- Automatically detects whether to compress or decompress based on input

## Features

- **Run-length encoding**: Groups of repeated letters are compressed as count + letter.
- **Automatic mode detection**: Expands compressed strings or compresses expanded strings.
- **Supports multi-digit counts** (e.g. `"12a"` for twelve `'a'`s)
- **Handles edge cases** and invalid input (with optional validation still in progress).

## Usage

```python
from decompress import DeCompress  # or your module name

# Compress a string
dc = DeCompress("aaabbbcccc")
print(dc.initialize())  # Output: "3a3b4c"

# Decompress a string
dc = DeCompress("3a3b4c")
print(dc.initialize())  # Output: "aaabbbcccc"
