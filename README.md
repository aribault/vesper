# Vesper

A hands-on exploration of autoregressive language models from first principles. The goal is to understand their mathematics, internal mechanisms, and computational trade-offs by implementing and validating the essential components—not to build a competitive model.

## Philosophy

**Understand it first. Implement it yourself. Validate it. Then optimize it.**

Each milestone combines mathematical reasoning, a focused implementation, correctness checks, and small experiments. Testing and performance analysis are part of learning: every important component should have explainable mathematical and computational behavior.

Python is the primary language. We begin with a small automatic differentiation engine to understand backpropagation, then use PyTorch tensor operations and eventually autograd for larger models. Attention, normalization, embeddings, feed-forward networks, optimizers, tokenizers, training loops, and generation strategies are implemented manually as learning exercises.

Prebuilt Transformer frameworks should not bypass those exercises. Optimized built-ins can later serve as references for validation and benchmarking. Rebuilding tensor engines, GPU kernels, or a complete numerical framework is not a prerequisite; technical choices should serve the learning objective.

## Learning roadmap

The sequence is incremental and may evolve as experiments reveal useful questions.

1. **Automatic differentiation:** computational graphs, the chain rule, gradient accumulation, and backpropagation in a small scalar engine.
2. **Language modeling foundations:** next-token prediction, likelihood, cross-entropy, and simple baseline models.
3. **Tokenization:** text representations, vocabulary construction, encoding and decoding, and a manually implemented tokenization algorithm.
4. **Neural building blocks:** embeddings, linear layers, activations, normalization, and feed-forward networks, including shape and numerical considerations.
5. **Transformers:** positional information, causal self-attention, multiple heads, residual connections, and a small autoregressive model.
6. **Optimization and training:** manually implemented optimizers and training loops, gradient checks, tiny-data convergence, and reproducible experiments.
7. **Generation:** autoregressive decoding, sampling strategies, and their effects on output and cost.
8. **Inference and efficiency:** KV caching, runtime and memory measurements, and comparisons with optimized implementations.

Correctness and understanding come before scale. Milestones should build on components that have already been implemented and validated, with minimal early abstraction or infrastructure.

## Experiment constraints

Development targets an Apple Silicon MacBook Air with 16 GB of unified memory. Initial exercises favor CPU execution, small models, synthetic or tiny datasets, and short runs. Demonstrating a correct gradient, convergence on a tiny dataset, or a measurable trade-off is a successful outcome.

Avoid prolonged local workloads. Cloud GPUs are reserved for experiments with clear educational value, within an approximate total budget of €25–30. Dependency installation, training jobs, and substantial dataset downloads require explicit approval; paid cloud operations and expensive compute always require explicit approval.

## Collaboration

The learner writes all implementation code; the assistant acts as a technical mentor. Guidance includes theory, algorithms, pseudocode, API references, validation ideas, and code review. The assistant never edits implementation files. Implementation code is provided only when explicitly requested and only in chat.

Persistent collaboration rules are in [AGENTS.md](AGENTS.md).

## Status and license

Documentation setup only; implementation has not started. The proposed first milestone is a small scalar automatic differentiation engine.

Licensed under the [MIT License](LICENSE).
