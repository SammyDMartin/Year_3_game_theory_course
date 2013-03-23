# This file was *autogenerated* from the file L06-plot02.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0)#!/usr/bin/env

p = plot(_sage_const_1 -_sage_const_2 *x,x,_sage_const_0 ,_sage_const_1 ,legend_label="$u_2(\sigma_1,s_1)$", color='red')
p += plot(_sage_const_2 *x-_sage_const_1 ,x,_sage_const_0 ,_sage_const_1 ,legend_label="$u_2(\sigma_1,s_2)$", color='blue')
p.axes_labels(['$x$','$u$'])
p.save("L06-plot02.png")
