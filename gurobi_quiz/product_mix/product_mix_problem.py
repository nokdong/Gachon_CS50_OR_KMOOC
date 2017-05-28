from gurobipy import *

def modelling():
    m = Model("product_mix_problem_model")
    # === Modify codes below using above variable m ===





    # ================================================
    m.optimize()
    return m

if __name__ == "__main__":
    model_object = modelling()
    for v in model_object.getVars():
        print(v.varName, v.x)

    print('Obj:', model_object.objVal)