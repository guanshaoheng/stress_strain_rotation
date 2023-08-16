
# 应力应变张量共轴性讨论
This is a script to verify that the principal directions of strain and stress tensor will not change under the isotropic elastic assumptions. 

代码请查看[点击](https://github.com/guanshaoheng/stress_strain_rotation).

# 弹性假设下
弹性假设下，应力计算公式可记为：
$ \sigma_{ij} = D_{ijkl} \epsilon_{kl} = K\epsilon_v \delta_{ij} + 2G(\epsilon_{ij} - \delta_{ij}\epsilon_v/\mathrm{ndim})$

其中，体积应变$\epsilon_v =\epsilon_{kk}$,右手边第一项为静水压力项，不影响方向，第二项的方向与应力方向相同。因此，在弹性假设下，二者方向相同。

**或者说应力的方向与弹性应变的方向是相同的。**

# 塑性出现

一旦有塑性应变$\epsilon_{ij}^p = d\lambda\frac{\partial g}{\partial \sigma_{ij}}$出现，则应变总量表示为
$\epsilon_{ij} = \epsilon_{ij}^e + \epsilon_{ij}^p$

塑性应变可分解为塑性剪应变和体积应变：
$\epsilon_{ij}^{p} = e_{ij}^p + \epsilon_v^p \delta_{ij}$
其中，塑性体积应变不会影响方向。所以，检查弹性件应变和塑性剪应变的方向是否重合，如果二者重合，则总体剪应变可以表示为：
$e_{ij} = e^e_{ij} + e^{p}_{ij} = (1 + n)e^e_{ij}$
因此，当且仅当弹性剪应变$e^e_{ij}$与塑性剪应变$e^p_{ij}$方向相同的时候，应力和应变张量的主轴还重合。

但是塑性剪应变的方向由塑性势函数对应力的偏导数决定
$\epsilon_{ij}^p = d\lambda\frac{\partial g}{\partial \sigma_{ij}}$
所以，当塑性出现的时候，二者的主轴不再重合。

# 文献中的共轴性处理

但是在一些文献中，作者假设在发生塑性变形后，整体应变张量$\epsilon_{ij}$仍然与应力张量$\sigma_{ij}$的主方向重合.

但是，也有一些巧妙地处理，在文献[Vlassis, N. N., & Sun, W. C. (2021).](https://doi.org/10.1016/j.cma.2021.113695)中，应力的处理为
![Vlassis 2021](image.png)
- 假设应变增量为弹性，添加该应变到整体的弹性应变上；
- 弹性应变谱分解（旋转到主方向），三个特征值即为主方向的应变大小；
- 通过应力与弹性应变共轴可以通过势函数(超弹性)计算出尝试的弹性应力三个主轴上的值；
- 将尝试应力的主轴的值带入屈服函数进行塑性修正(Plastic return mapping)；
- 回归计算出对应的弹性应变的三个主轴值；
- 然后通过势函数计算应力的三个主轴值；
- 然后通过尝试弹性应变的谱分解得到的Eigen Vector将应力升维到三维。

实际上，此处带有一个假设：**下一步的应力的方向与当前应变的弹性部分和尝试应变增量的和的方向相同**。

如果上一荷载步为全弹性，无论下一荷载步是否发生塑性变形，下一步的应力张量与 $\epsilon_{ij} + \Delta \epsilon_{ij}$ 共轴。

但是，由于在塑性修正中更新了$ \epsilon_1^e, \epsilon_2^e, \epsilon_3^e $，在下一步，应力的张量不会与应变张量共轴。这种将弹性应变分离出来的方法也出现在文献[Tang, S., Zhang, G., Yang, H., Li, Y., Liu, W. K., & Guo, X. (2019)](https://doi.org/10.1016/j.cma.2019.112587)中.

**也就是说，应力只与弹性应变张量共轴。所以在数据驱动的工作中，还是要简历理论用于更新塑性修正后的弹性应变部分。**