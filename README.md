# Protocol Parser Complexity Hierarchy (PPCH)

Companion repository for the ICNP 2026 paper:
**"A Complexity Hierarchy for Protocol-Parser Inference: Foundations and Security Implications"**

---

## Overview

This repository provides the formal framework, protocol specifications, and evaluation code for the Protocol-Parser Complexity Hierarchy (PPCH) — a system for classifying the structural complexity of network protocol parsers into four tiers based on inter-field dependencies.

| Tier | Name | Dependency |
|------|------|-----------|
| 0 | Static | None — fixed field sequence |
| 1 | Conditional | Message-type field governs payload structure |
| 2 | Length-Based | A length field governs a dependent field's size |
| 3 | Recursive | A count field governs repeated field sequences |

---

## Repository Structure

```
├── SPECs/               # Protocol specifications in PPCH notation (.spec files)
├── CSVs/                # Protocol metadata and CVE datasets
├── PDFs/                # DFA visualisations per protocol
└── README.md
```

---

## Protocol Specifications

Specifications for 50 real-world protocols are provided in `SPECs/`, manually constructed from RFCs and existing parser implementations (Wireshark, Scapy). Each `.spec` file uses our human-readable notation:

```
# Field type declarations
Fix(32)/uint  : SequenceNumber Length
Del(8,0x00)/ascii : Method URI

# Hierarchical structure (BNF-style)
Packet = Header Payload

# Conditional dependency
Payload = ? case *MessageType
  | 0 RequestFormat
  | 1 ResponseFormat
?

# Length-based dependency
Body = Len(*Length) Content

# Recursive dependency
Items = Item^*Count
```

---

## DFA Construction

Each protocol specification is compiled into a Deterministic Finite Automaton (DFA) using pyformlang. The parser DFA is defined as the 5-tuple (Q, B, δ, s, F) over the binary alphabet B = {0, 1}, extended with a field mapping λ : Q → F.

Field framings map to sub-DFAs as follows:

- `Fix(n)` — n-bit fixed-length field
- `Del(n, C)` — delimiter-terminated field in n-bit chunks
- `Set(A, B, ...)` — field accepting a specific set of bit strings
- `EOF` — consumes all remaining bits

Complex inter-field dependencies (conditional, length-based, recursive) are composed via DFA union (∪), intersection (∩), concatenation (⊕), and set exclusion (\).

---

## CVE & IDS Analysis

The `CSVs/` directory contains the dataset of 278 Suricata signatures across 90 CVEs and 34 erroneous protocol implementations, annotated with:

- Protocol name and PPCH tier
- CWE classification
- Rule creation date, revision count, and days-per-revision
- CVE signature average log density

This data supports the empirical findings in Section V of the paper:
- Higher-tier protocols produce a greater diversity of CWE vulnerability classes.
- Tier 1 and 2 protocol rules go unrevised **18 months longer** on average than the non-parser baseline.
- **70%** of parser-CVE signatures match only a single fixed payload (average log density = 0).

---

## Metrics

**Parsability** quantifies deviations between an inferred DFA and the true protocol DFA:
- *Underparsing* — valid packets rejected by the inferred parser
- *Overparsing* — invalid packets accepted by the inferred parser

Both are measured via average log density h(M), the proportion of bits free to vary across accepted strings of each length.

**Agreement** compares inferred field mappings to ground truth at the bit level (micro) and field level (macro), across framing, syntax, and semantics independently.

---