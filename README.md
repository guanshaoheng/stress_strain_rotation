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
