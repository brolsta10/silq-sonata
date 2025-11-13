from typing import Callable, Optional

class Sonata:
    """
    Orchestrates: story (libretto) -> quantum score (Silq-like pseudocode)
    """
    def __init__(self, llm_call: Callable[[str], str]):
        self.llm_call = llm_call

    def interpret(self, libretto: str, style: str = "silq") -> str:
        prompt = f"""
You are a quantum poet-engineer.
Translate the following story into Silq-like pseudocode (not exact Silq).
Constraints:
- Only use amplitudes, phases, entanglement, measurement concepts.
- Keep code minimal and composable.
- Use comments as metaphors that mirror intent.
- Prefer: fresh(), h(), rz(theta), cnot(a,b), measure(q), return values.
- Avoid non-quantum fluff; keep identifiers simple and musical.

STORY:
{libretto}

FORMAT:
- Start with 'silq//' header comments.
- One or more def blocks.
- A small entry (def main or def run_story) returning a value or printing a line.
"""
        return self.llm_call(prompt).strip()
