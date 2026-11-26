# Stanton 1999 年 Conjecture 12 的来源与无穷反例族

**论文：** *An infinite family of counterexamples to Stanton's polynomial positivity conjecture*  
**作者：** Zizhou Zhang（张子周）  
[阅读英文短文](paper.pdf) · [LaTeX 源文件](paper.tex) · [精确核验脚本](verify_example.py)

## 猜想从哪里来

Dennis Stanton 在 *Open positivity conjectures for integer partitions*, *Trends in Mathematics* **2** (1999), 19–25 的 **Conjecture 12** 中提出：给定正整数 $a_1,\ldots,a_n$，令 $N=\sum_{i=1}^n a_i$，如果

$$
\frac{\prod_{j=1}^{N}(1-q^j)}{\prod_{i=1}^{n}(1-q^i)^{a_i}}
$$

是多项式，则其系数全部非负。

- [Stanton 作者原文](https://www-users.cse.umn.edu/~stant001/PAPERS/korea99.pdf)：PDF 第 6 页，对应期刊第 24 页，Conjecture 12。

这里不要求序列对称或递减。同页有关对称性及所有平移参数的要求属于另一个猜想 **Conjecture 11**，不属于 Conjecture 12。

## 本文展示的例子

短文先展示以下显式反例及其证明，再推广为无穷反例族：

$$
Q(q)=\frac{(1-q^{277})(1-q^{278})(1-q^{279})(1-q^{280})}
{(1-q^{10})(1-q^{56})(1-q^{93})(1-q^{139})}.
$$

它是次数 $816$ 的整系数多项式，却满足 $[q^{277}]Q(q)=-1$。在原猜想中，取 $n=276$，令 $a_{10}=a_{56}=a_{93}=a_{139}=2$，其余 $a_i=1$，便有 $N=280$，约分后正好得到 $Q(q)$。

证明分两步：逐圆分因子验证多项式性；再用奇偶性和模 $5$ 的论证排除 $277$ 的非负整数表示，从而得到负系数。

## 无穷反例族

对任意整数 $r\geq0$，令 $m=30r+28$，定义

$$
Q_r(q)=\frac{\prod_{j=10m-3}^{10m}(1-q^j)}
{(1-q^{10})(1-q^{2m})(1-q^{5m-1})(1-q^{(10m-1)/3})}.
$$

论文证明，对每个 $r\geq0$ 都有

$$
Q_r(q)\in\mathbb Z[q],\qquad
\deg Q_r=890r+816,\qquad
[q^{300r+277}]Q_r(q)=-1.
$$

各多项式次数严格递增，因此得到无穷多个不同的反例；$r=0$ 就是上面的显式例子。它们在原猜想中的参数为 $n=300r+276$、$N=300r+280$，在四个分母权处取 $a_i=2$，其余位置取 $a_i=1$。

随附脚本对 $r=0,1,2,3,10,100$ 做精确整数核验，包括多项式完整乘回和原猜想参数匹配。这些有限计算是补充核验；所有参数的结论由正文中的统一证明建立。

## 构造来源与 AI 参与

本文的显式反例及整个无穷反例族完全由 **OpenAI's Codex（GPT-6）** 构造。AI 还参与了证明探索、计算、写作及内部一致性核查。论文署名为 **Zizhou Zhang**，作者对论文内容负责；内部自动核查不等同于外部专家审阅。

The explicit counterexample and the infinite family of counterexamples presented in this paper were constructed entirely by OpenAI's Codex (GPT-6).

这些反例否定的是 Stanton 的 Conjecture 12，不是同上标的 Gatzweiler–Krattenthaler Gaussian 二项式商猜想。
