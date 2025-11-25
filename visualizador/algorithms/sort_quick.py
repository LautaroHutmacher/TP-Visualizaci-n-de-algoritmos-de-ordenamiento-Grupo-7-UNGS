# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
stack = []
lo = hi = pivot = i = j = pi = None
phase = None

def init(vals):
    global items, stack, lo, hi, pivot, i, j, pi, phase
    items = list(vals)
    stack = []
    if len(items) > 1:
        stack.append((0, len(items) - 1))
    lo = hi = pivot = i = j = pi = None
    phase = None

def step():
    global items, stack, lo, hi, pivot, i, j, pi, phase

    # 1) Caso base: no hay más trabajo
    if phase is None and not stack:
        return {"done": True, "swap": False}

    # 2) Si no hay fase activa, iniciar siguiente rango
    if phase is None:
        lo, hi = stack.pop()
        if hi - lo < 1:
            return {"a": lo, "b": lo, "swap": False, "done": False}
        pivot = items[hi]   # pivote Lomuto
        i = lo
        j = lo
        phase = "scan"

    # 3) Escaneo de la partición
    if phase == "scan":
        if j < hi:
            if items[j] <= pivot:
                items[i], items[j] = items[j], items[i]
                a, b = i, j
                i += 1
                j += 1
                return {"a": a, "b": b, "swap": True, "done": False}
            else:
                a, b = j, hi
                j += 1
                return {"a": a, "b": b, "swap": False, "done": False}
        else:
            phase = "final_swap"

    # 4) Swap final del pivote
    if phase == "final_swap":
        items[i], items[hi] = items[hi], items[i]
        a, b = i, hi
        pi = i
        phase = "push"
        return {"a": a, "b": b, "swap": True, "done": False}

    # 5) Empujar subrangos
    if phase == "push":
        if pi + 1 < hi:
            stack.append((pi + 1, hi))
        if lo < pi - 1:
            stack.append((lo, pi - 1))
        phase = None
        return {"a": pi, "b": pi, "swap": False, "done": False}