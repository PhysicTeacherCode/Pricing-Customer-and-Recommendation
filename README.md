# Pricing, Customer Behavior and Recommendation Strategies

Este repositório é um compilado de estratégias fundamentadas em **dados, estatística, economia e machine learning**, com o objetivo principal de resolver problemas complexos na área de **Pricing** (precificação).

O projeto aborda desde a limpeza e preparação dos dados até a implementação de modelos de sensibilidade de preço, análise de sazonalidade, classificação de clientes e sistemas de recomendação.

## 💾 Dataset:

* `Fonte`: [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail)
* `Descrição`: Registro de vendas de um site de varejo contendo mais 50 mil registros de compras de mais 4000 clientes em 37 países.

## 📁 Estrutura do Repositório:

*   `data/`: Contém os conjuntos de dados utilizados nas análises.
*   `notebooks/`: Jupyter Notebooks com o passo a passo de cada estratégia e modelo.
*   `src/`: Scripts Python para automação de limpeza e criação de datasets.

## 📚 Conteúdo dos Notebooks:

A análise está dividida em seis etapas principais:

1.  **Limpeza de Dados (`1_cleaning_data.ipynb`)**: Processamento inicial e preparação da base de dados.
2.  **Sensibilidade de Preço (`2_pricing_sensitivity.ipynb`)**: Análise de como variações no preço impactam a demanda (Elasticidade-Preço).
3.  **Trade-off de Preço (`3_price_trade_off.ipynb`)**: Estudo do equilíbrio entre volume de vendas e receita.
4.  **Efeito de Sazonalidade (`4_seazonality_effect.ipynb`)**: Identificação de padrões temporais.
5.  **Classificação de Clientes (`5_customer_classification.ipynb`)**: Clusterização de clientes para estratégias de vendas personalizadas.
6.  **Recomendação de Produtos (`6_product_recommendation.ipynb`)**: Recomendação de produtos com base no comportamento de compra.

## 📊 Resultados:

### Distribuição de produtos de acordo com preço médio e a demanda:
![Preço e Quantidade](reports/price_quantity.png)

### Distribuição de receita por dia de cada mês com maiores vendas:
![Melhores Meses Receita](reports/highest_months_revenue.png)

### Heatmap que indica quais dias da semana de cada mês receberam mais receita:
![Heatmap Semanal](reports/heatmap_semanal.png)

### Distribuição RFM por cluster de clientes:
![Cluster de Cliente](reports/kmeans_clusters.png)

## 🛠️ Tecnologias Utilizadas:

*   **Linguagem:** Python
*   **Bibliotecas de Dados:** Pandas, NumPy
*   **Visualização:** Matplotlib, Seaborn
*   **Machine Learning:** Scikit-learn
*   **Ambiente:** Jupyter Notebook

## 👤 Autor

**Diego de Lima Fernandes**
- LinkedIn: [linkedin.com/in/diegulus](https://www.linkedin.com/in/diegulus/)
- GitHub: [@PhysicTeacherCode](https://github.com/PhysicTeacherCode)
- Email: diego196095@gmail.com
