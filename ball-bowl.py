import sympy as sp

g, h, l, v, r, t = sp.symbols('g h l v r t')


a = 70
g = 9.8
h = 1.5
l = 2
r = sp.pi * a / 180


eq1 = sp.Eq(l, v * sp.cos(r) * t)
td = sp.solve(eq1, t)[0]

eq2 = sp.Eq(h, v * sp.sin(r) * t - (g * (t**2) / 2))
eq2_substituted = eq2.subs(t, td)
vd = sp.solve(eq2_substituted, v)[1]

eq1_substituted = eq1.subs(v, vd)

print(f"v = {vd}")
print(f"t = {sp.solve(eq1_substituted, t)}")