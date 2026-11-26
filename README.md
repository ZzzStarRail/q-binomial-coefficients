# q 二项式系数相关

**Q-binomial coefficients and related positivity questions**

Author: **Zizhou Zhang（张子周）**  
Academy of Mathematics and Systems Science, Chinese Academy of Sciences, Beijing, China

本仓库收录两篇英文预印本及其 LaTeX 源文件。每个子目录的说明介绍原猜想的出处、准确表述和本文结果。

| 论文 | 结果 | 文件 |
| --- | --- | --- |
| *An interval semigroup criterion and positivity of polynomial Gaussian binomial quotients* | 证明 Gatzweiler–Krattenthaler 的同上标 Gaussian 二项式商非负性猜想 | [PDF](gatzweiler-krattenthaler/paper.pdf) · [LaTeX](gatzweiler-krattenthaler/paper.tex) · [来源说明](gatzweiler-krattenthaler/README.md) |
| *An infinite family of counterexamples to Stanton's polynomial positivity conjecture* | 给出 Stanton 1999 年 Conjecture 12 的显式反例及无穷反例族，并附完整证明 | [PDF](stanton-conjecture-12/paper.pdf) · [LaTeX](stanton-conjecture-12/paper.tex) · [来源说明](stanton-conjecture-12/README.md) |

The first manuscript proves the Gatzweiler–Krattenthaler conjecture for polynomial quotients of Gaussian binomial coefficients with the same upper argument. The second gives an explicit counterexample and an infinite family of counterexamples to Conjecture 12 in Stanton's 1999 paper. These are different assertions; the counterexamples do not contradict the Gaussian binomial result.

Stanton 论文中的显式反例及整个无穷反例族完全由 OpenAI's Codex（GPT-6）构造，文中已明确注明。论文由 Zizhou Zhang 署名，作者对论文内容负责。

The explicit counterexample and the infinite family in the Stanton manuscript were constructed entirely by OpenAI's Codex (GPT-6).

当前版本：2026 年 11 月 26 日。两篇论文均为作者预印本，尚未经过外部同行评审；AI 参与情况见各论文的专门说明。

## 编译与核验

在任一论文目录中，用常规 TeX Live 或 MiKTeX 环境运行两遍：

```sh
pdflatex paper.tex
pdflatex paper.tex
```

Stanton 短文的证明不依赖计算机。在该目录运行以下命令，可额外核验显式例子及反例族中 $r=0,1,2,3,10,100$ 的圆分指数、完整系数和多项式恒等式。脚本只用 Python 标准库；所有 $r\geq0$ 的结论由论文中的统一证明建立。

```sh
python verify_example.py
```

原始文献的链接均列在论文及来源说明中。
