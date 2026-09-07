# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

I installed and authenticated the tool.
copilot --version
GitHub Copilot CLI 1.0.82.

### Antigravity CLI

I installed and authenticated the tool.
agy --version
1.1.23

## Shared task

### Shared prompt

### Shared prompt

Paste the exact prompt you submitted to both CLI tools.

```text
Implement this Python function. Return the complete function with its docstring in a single ```python code block, followed by two or three sentences explaining your approach and any edge cases you considered.

def count_vowels(text: str) -> int:
    """Count a, e, i, o, and u without regard to case; do not count y."""
```

### Copilot CLI observations

The approach normalizes uppercase and lowercase letters to be treated the same way, while excluding "y", and appears to  handle everything else such as empty strings naturally. I would want to verify if it handles cases like empty strings naturally, as well as question what it means by naturally. Another question would be whether or not if vowels with special characters will be treated similarly or differently.

### Antigravity CLI observations

This approach ensures that all string inputs are in lowercase form so that it can check for vowels excluding "y", and it also naturally handles cases of things like empty strings. This approach summary explicitely states it also handles strings with consonants or symbols. I would like to verify that, and I also question what it means by "constant-time lookups," whether that means the script constantly runs through itself to ensure accuracy or if it means something different.

### Comparison

Both responses highlight specific callouts such as the normalization or conversion of uppercase and lowercase letters and or the exclusion of the letter "y," to ensure that the vowels are being counted correctly. The responses are different in the sense that they view the vowels differently, since Copilot views them as a string ('aeiou'), and Antigravity views them as a set ({"a", "e", "i", "o", "u"}). Antigravity's responses also uses more specific language than Copilot's, making it easier to understand the specific approach of the CLI. The assumptions differed in that Copilot stripped punctuation while Antigravity never even bothered to touch it. I selected Antigravity's response because of the usefulness it provided in terms of explaining how the code will be ran through.

## Test-guided implementation

Running the grader the first time produced nine passing tests and four failures, wherefour failures were for the same reason, that being that the journal still contained the template's original responses since I hadn't inputted my own summaries yet. The Python tests told a different story where test_vowels_are_case_insensitive, test_text_with_no_vowels, and test_empty_text all passed, confirming that count_vowels handled uppercase input, consonant-only strings, and empty text correctly. I revised the implementation after comparing the two CLI suggestions, replacing the string "aeiou" with Antigravity's set since I thought it to be more understanding. The final behavior matches the vowel count coding line in that the five specified vowels are counted, "y" is excluded, capitalization is ignored, and an int is returned.

## Preferred tool combination

In my opinion I found browser chat to be extremely helpgul because it allowed me to look up what certain lines or areas of code meant without actually doing the work for me, giving me a better understanding as a whole. Copilot CLI was straighforward and quick, however I found the summary of the prompt to be a little ocnfusing. Antigravity CLI required me to clear everything before I could begin a conversation, however the instructions were clearer and more specific to the prompt in my opinion, which is why I stuck with that once specifically instead of combining methods from the two CLIs. For my perosnal workflow, I enjoy browser chat for understanding what's happening, and I enjoy using CLIs to help me generate the code so I can review it myself in case I have any concerns or questions.