# Gatzweiler–Krattenthaler 猜想的来源与本文结果

**论文：** *An interval semigroup criterion and positivity of polynomial Gaussian binomial quotients*  
**作者：** Zizhou Zhang（张子周）  
[阅读英文论文](paper.pdf) · [LaTeX 源文件](paper.tex)

## 猜想从哪里来

Mona Gatzweiler 与 Christian Krattenthaler 在 *A positivity conjecture for a quotient of q-binomial coefficients* 的 **Conjecture 1** 中提出：对 $0\leq k,\ell\leq n$，若

$$
\frac{\binom{n}{k}_q}{\binom{n}{\ell}_q}
$$

是多项式，则其系数全部非负。

原论文首个 arXiv 版本发表于 **2025 年 2 月 9 日**；正式期刊信息为 *The Ramanujan Journal* **69** (2026), Article 13。

- [原论文 arXiv:2502.06032](https://arxiv.org/abs/2502.06032)
- [正式期刊版本](https://doi.org/10.1007/s11139-025-01285-2)

Gatzweiler、Levicán-Santibáñez 与 Yoshida 后来给出了基于加权正则序列和半群表示计数的判据，并在其 **Corollary 3.10** 中证明包括 $n\geq k^2$ 在内的参数范围。本文使用其 **Propositions 3.3 和 3.6** 作为从半群计数到系数非负性的桥梁。

- [该判据及部分结果，arXiv:2603.22226v1](https://arxiv.org/abs/2603.22226v1)

## 本文做了什么

本文证明一个区间半群计数定理：对于互异的正整数生成元，若生成元均位于目标区间之前、生成元直径小于区间长度，而且所有整除计数条件成立，则区间中有足够多的半群可表示整数。其证明结合 Kneser 加法定理与显式同余类表示。

将这个定理用于 Gaussian 二项式商约分后的两个整数区间，可验证每个分母子集所需的条件，从而证明上述 Conjecture 1 的完整陈述。本文结果保留直径条件和生成元互异条件；它不声称任意乘积商只要成为多项式就必有非负系数。

这也解释了同仓库 Stanton 反例与本文结论相容：该反例的分母支持直径为 $139-10=129$，分子区间长度仅为 $4$，不满足本文区间定理的直径条件。
