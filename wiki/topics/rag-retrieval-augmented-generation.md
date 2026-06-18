# RAG (Retrieval-Augmented Generation)

**Type:** Topic
**Status:** stub
**Last updated:** 2026-05-31
**Sources:** [karpathy-llm-wiki-2026]

## Summary

Retrieval-Augmented Generation (RAG) is an AI pattern where a language model is augmented with a retrieval step: relevant chunks from a document corpus are fetched (via vector search) and injected into the prompt at query time. The LLM Wiki pattern is an explicit alternative to RAG for personal research knowledge bases, trading retrieval infrastructure for a pre-compiled, fully synthesized wiki.

## Key Facts / Claims

- RAG requires vector databases, embedding pipelines, and retrieval infrastructure [karpathy-llm-wiki-2026]
- The LLM Wiki pattern is reported to be ~70x more token-efficient than RAG for repeated queries on a stable knowledge base [karpathy-llm-wiki-2026]
- RAG retrieves raw chunks; LLM Wiki queries a pre-synthesized, cross-linked artifact — giving richer context per token [karpathy-llm-wiki-2026]

## Connections

- [[llm-wiki-pattern]] — LLM Wiki is positioned as the alternative to RAG for personal/research knowledge management

## Open Questions

- At what scale does RAG outperform the LLM Wiki pattern (e.g., corpus too large for a single context window)?
- How do hybrid approaches (RAG over the compiled wiki) perform vs. either alone?

## Raw Notes

See also: LLM Wiki v2 community extension: https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2
