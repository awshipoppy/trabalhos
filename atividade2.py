import numpy as np  # Importa a biblioteca NumPy para operações matemáticas e matriciais
from scipy.linalg import lu  # Importa a função LU para decomposição de matrizes

# ==============================
# Fatoração LU
# ==============================
def lu_method(A, b):
    """
    Resolve um sistema linear Ax = b usando a decomposição LU.
    """
    print("\n>>> Fatoração LU")
    P, L, U = lu(A)  # Decomposição LU da matriz A, onde P é a matriz de permutação, L é triangular inferior, U é triangular superior
    
    print("Matriz L:")
    print(L)  # Exibe a matriz triangular inferior
    print("Matriz U:")
    print(U)  # Exibe a matriz triangular superior
    print("Matriz P:")
    print(P)  # Exibe a matriz de permutação

    y = np.linalg.solve(L, np.dot(P, b))  # Resolve o sistema Ly = Pb por substituição progressiva
    print("Resolvendo Ly = Pb:")
    print("y =", y)

    x = np.linalg.solve(U, y)  # Resolve Ux = y por substituição regressiva
    return x

# ==============================
# Eliminação de Gauss
# ==============================
def gauss_elimination(A, b):
    """
    Resolve um sistema linear Ax = b pelo método de Eliminação de Gauss.
    """
    print("\n>>> Eliminação de Gauss")
    Ab = np.hstack((A.astype(float), b.reshape(-1, 1)))  # Cria a matriz aumentada [A | b]
    n = len(b)  # Obtém o número de variáveis do sistema
    
    # Fase de eliminação
    for i in range(n):
        print(f"\nEtapa {i+1} - Pivô em A[{i}][{i}] = {Ab[i][i]}")
        for j in range(i + 1, n):  # Eliminação das variáveis abaixo do pivô
            fator = Ab[j][i] / Ab[i][i]  # Calcula o multiplicador
            Ab[j, i:] = Ab[j, i:] - fator * Ab[i, i:]  # Subtrai a linha escalonada
            print(f"L{j+1} = L{j+1} - ({fator:.3f}) * L{i+1}")
            print("Matriz após eliminação:")
            print(Ab)

    # Substituição regressiva
    x = np.zeros(n)  # Inicializa o vetor solução
    for i in range(n - 1, -1, -1):  # Percorre de trás para frente
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:n])) / Ab[i, i]  # Resolve para x[i]
    return x

# ==============================
# Método de Jacobi
# ==============================
def jacobi(A, b, x0=None, tol=1e-3, max_iter=100):
    """
    Resolve um sistema linear Ax = b pelo método iterativo de Jacobi.
    """
    print("\n>>> Método de Jacobi")
    n = len(b)  # Número de variáveis
    x = np.zeros_like(b) if x0 is None else x0.copy()  # Inicializa x com zeros ou valor inicial dado

    for k in range(1, max_iter + 1):
        x_new = np.zeros_like(x)  # Inicializa o novo vetor de soluções
        print(f"\nIteração {k}")
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)  # Soma dos termos da linha sem o pivô
            x_new[i] = (b[i] - s) / A[i][i]  # Atualiza x[i]
            print(f"x[{i+1}] = ({b[i]} - {s}) / {A[i][i]} = {x_new[i]:.6f}")
        
        erro = np.linalg.norm(x_new - x, ord=np.inf)  # Calcula erro pelo máximo valor absoluto
        print(f"Erro: {erro:.6e}")
        if erro < tol:
            print("Convergência alcançada com erro menor que 0.001.")
            break
        x = x_new  # Atualiza x
    return x

# ==============================
# Método de Gauss-Seidel
# ==============================
def gauss_seidel(A, b, x0=None, tol=1e-3, max_iter=100):
    """
    Resolve um sistema linear Ax = b pelo método de Gauss-Seidel.
    """
    print("\n>>> Método de Gauss-Seidel")
    n = len(b)
    x = np.zeros_like(b) if x0 is None else x0.copy()

    for k in range(1, max_iter + 1):
        x_old = x.copy()
        print(f"\nIteração {k}")
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(i))  # Soma dos valores já atualizados
            s2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n))  # Soma dos valores antigos
            x[i] = (b[i] - s1 - s2) / A[i][i]  # Atualiza x[i]
            print(f"x[{i+1}] = ({b[i]} - {s1} - {s2}) / {A[i][i]} = {x[i]:.6f}")
        
        erro = np.linalg.norm(x - x_old, ord=np.inf)  # Calcula erro
        print(f"Erro: {erro:.6e}")
        if erro < tol:
            print("Convergência alcançada com erro menor que 0.001.")
            break
    return x

# ==============================
# Entrada do sistema linear
# ==============================
def input_system():
    """
    Solicita ao usuário a entrada da matriz A e do vetor b.
    """
    n = int(input("Quantas variáveis (n)? "))
    print("Digite a matriz A (linha por linha, valores separados por espaço):")
    A = [list(map(float, input(f"A[{i+1}]: ").split())) for i in range(n)]
    
    print("Digite o vetor b:")
    b = list(map(float, input("b: ").split()))
    return np.array(A), np.array(b)

# ==============================
# Menu principal
# ==============================
def main():
    """
    Exibe o menu e executa o método escolhido pelo usuário.
    """
    print("=== RESOLUÇÃO DE SISTEMAS LINEARES ===")
    A, b = input_system()
    
    print("\nEscolha o método numérico:")
    print("1 - Fatoração LU")
    print("2 - Eliminação de Gauss")
    print("3 - Iterativo de Jacobi")
    print("4 - Iterativo de Gauss-Seidel")

    opcao = input("Método (1-4): ")
    metodos = {'1': lu_method, '2': gauss_elimination, '3': jacobi, '4': gauss_seidel}
    x = metodos.get(opcao, lambda A, b: print("Opção inválida."))(A, b)
    
    print("\nSolução final:")
    for i, xi in enumerate(x):
        print(f"x{i+1} = {xi:.6f}")

if __name__ == "__main__":
    main()
