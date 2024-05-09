
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados do arquivo gasolina.csv
df = pd.read_csv("gasolina.csv")

# Gerar o gráfico de linha
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.lineplot(x="dia", y="venda", data=df, marker="o", color="b", linewidth=2.5)
plt.title("Preço da gasolina ao longo dos dias")
plt.xlabel("Dia")
plt.ylabel("Preço (R$)")
plt.grid(True)

# Salvar o gráfico como gasolina.png
plt.savefig("gasolina.png")
