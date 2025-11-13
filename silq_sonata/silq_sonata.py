from sonata import Sonata
from orchestra import Orchestra, OrchestratorConfig
from perform import Performer

def default_llm_call(prompt: str) -> str:
    return """silq// Two qubits: Alice (light) and Bob (shadow)
def soulBond(alice: qbit, bob: qbit) -> (qbit, qbit) {
    alice := h(alice);           // light reaches through the fog
    cnot(alice, bob);            // when one whispers, the other hears
    return (alice, bob);         // entanglement holds
}

def truth(): bool {
    a, b := soulBond(fresh(), fresh());
    ma := measure(a);
    mb := measure(b);
    return ma == mb;             // the echo of the soul
}

def run_story(): string {
    return "The bond is real: " + (truth() ? "true" : "false");
}
"""

def compose_and_run(libretto: str) -> str:
    sonata = Sonata(default_llm_call)
    score = sonata.interpret(libretto)
    orch = Orchestra(OrchestratorConfig(auto_uncompute=True, verify_with="z3"))
    silq_code = orch.compile_score(score)
    perf = Performer("soulbond.slq")
    return perf.perform(silq_code)

if __name__ == "__main__":
    story = """
In the silence between heartbeats, a single photon dances.
It splits, becomes two, then four—a choir of light.
Each voice sings a different future.
Listen closely: only one path rings true.
"""
    print(compose_and_run(story))
