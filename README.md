##LR1_ANALYZER

#### What is this?
An LR parser is a parser for the source code of programs written in a programming language that reads the input stream from left to right and produces the most right-handed output of a context-free grammar. The term LR(k) is also used)- analyzer, where k expresses the number of unread preview characters in the input stream, on the basis of which decisions are made in the analysis. Usually k is equal to 1 and is often omitted.
An LR parser can be created from a context-free grammar by a program called a parser generator, or it can be written manually by a programmer. A context-free grammar is classified as LR (k) if LR(k) exists)- an analyzer for it, as defined by the analyzer generator.

It is said that the LR parser performs bottom-up parsing because it tries to derive the grammar's top-level output by building it out of leaves.

A deterministic context-free language is a language for which some LR(k) grammar exists. Each LR (k) grammar can be automatically converted to an LR(1) grammar for the same language, while an LR (0) grammar for some languages may not exist. LR (0)-languages are a proper subset of deterministic ones.

The LR analyzer is based on an algorithm driven by an analysis table, a data structure that contains the syntax of the language being analyzed. Thus, the term LR analyzer actually refers to a class of analyzers that can parse almost any programming language for which an analysis table is provided. The analysis table is created by the parser generator.

LR analysis can be generalized as an arbitrary analysis of a context-free language without loss of performance, even for LR (k) grammars. This is due to the fact that most programming languages can be expressed by an LR (k) grammar, where k is a small constant (usually 1). Note that parsing non-LR (k) grammars is an order of magnitude slower (cubic instead of quadratic with respect to the size of the input stream).