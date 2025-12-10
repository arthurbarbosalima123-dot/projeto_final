# Projeto Fome Zero – Análise de Dados e Dashboard Estratégico

## 1. Problema de Negócio

A Fome Zero é uma empresa de tecnologia que opera como um marketplace de restaurantes, conectando **restaurantes**, **entregadores** e **clientes** em uma única plataforma. Por meio do aplicativo, usuários podem buscar restaurantes, solicitar pratos, fazer avaliações e utilizar serviços de entrega ou retirada.

Com o crescimento acelerado da plataforma, o CEO identificou uma grande dificuldade: **não existe visibilidade organizada dos principais indicadores estratégicos do negócio**. São gerados diariamente milhares de dados relacionados a preços, localidades, avaliações, tipos de culinária, entregas, reservas e outros fatores importantes.

Para melhorar a tomada de decisão e permitir que o CEO compreenda rapidamente o comportamento do marketplace, você foi contratado como **Cientista de Dados** para:

* Organizar, limpar e preparar os dados provenientes do arquivo `zomato.csv`.
* Desenvolver análises que respondam às principais perguntas do CEO.
* Construir um dashboard capaz de exibir as informações de maneira clara, visual e intuitiva.

O modelo de negócio é 100% marketplace, e as análises devem englobar **países**, **cidades**, **restaurantes** e **tipos de culinária**.

---

## 2. Premissas Assumidas para a Análise

* Os dados utilizados são os fornecidos no dataset *Zomato Restaurants Dataset*.
* Todos os registros passaram por tratamentos de limpeza, remoção de duplicidades e padronização dos nomes de colunas.
* A categorização de países, cores de avaliação e faixas de preço foi feita utilizando funções fornecidas no enunciado.
* Cada restaurante foi categorizado pelo **primeiro tipo de culinária listado**.
* Foram geradas diferentes visões analíticas para facilitar o entendimento do CEO sobre:

  * **Países**
  * **Cidades**
  * **Restaurantes**
  * **Tipos de culinária**

---

## 3. Estratégia da Solução

A solução foi construída com base nas principais visões do negócio, refletindo como o CEO deseja analisar a performance da Fome Zero.

### 🔵 Visão País

Indicadores analisados:

* País com mais cidades registradas.
* País com mais restaurantes cadastrados.
* País com mais restaurantes com preço nível 4.
* País com mais tipos de culinária distintos.
* País com maior quantidade total de avaliações.
* País com mais restaurantes que fazem entrega.
* País com mais restaurantes que aceitam reservas.
* Média de avaliações por país.
* Maior e menor nota média por país.
* Média do custo de um prato para duas pessoas por país.

### 🟢 Visão Cidade

Indicadores analisados:

* Cidades com mais restaurantes.
* Cidades com mais restaurantes com nota > 4.
* Cidades com mais restaurantes com nota < 2.5.
* Cidade com maior valor médio de prato para dois.
* Cidades com maior variedade de tipos de culinária.
* Cidades com mais restaurantes que fazem reservas, entregas ou pedidos online.

### 🔴 Visão Restaurantes

Indicadores analisados:

* Restaurante com mais avaliações.
* Restaurante com maior nota média.
* Restaurante com maior custo para duas pessoas.
* Restaurantes brasileiros com maior/menor nota.
* Comparações entre culinárias (ex: japonesa vs BBQ nos EUA).

### 🟡 Visão Tipos de Culinária

Indicadores analisados:

* Restaurantes com maior e menor nota média por tipo.
* Tipos de culinária com maior valor médio para duas pessoas.
* Tipos de culinária com mais restaurantes que aceitam pedidos online e entregas.

Cada análise foi estruturada com **pandas**, validada com tabelas e gráficos, e consolidada diretamente no dashboard final.

---

## 4. Top 3 Insights de Dados

1. **Restaurantes de culinária gourmet apresentam preços muito acima da média**, especialmente em países como Austrália e EUA.
2. **A concentração de restaurantes e avaliações é extremamente desigual**, com poucas cidades respondendo pela maior parte do movimento.
3. **A aceitação de pedidos online e entregas varia bastante entre os países**, indicando diferentes modelos de operação e maturidade digital.

---

## 5. O Produto Final do Projeto

O resultado foi a criação de um **dashboard interativo**, desenvolvido com **Streamlit**, que permite ao CEO:

* Navegar por diferentes visões estratégicas.
* Filtrar informações por país, cidade, preço e tipo de culinária.
* Analisar rapidamente métricas cruciais para a empresa.
* Visualizar rankings, tabelas, comparações e gráficos de forma intuitiva.

O dashboard está disponível online e acessível de qualquer dispositivo com internet.

*(Se você tiver link do seu dashboard, adicione aqui.)*

---

## 6. Conclusão

O projeto conseguiu organizar e transformar os dados brutos do Zomato em informações claras e úteis para tomada de decisão. As visões desenvolvidas permitiram ao CEO:

* Entender a distribuição global da empresa.
* Comparar desempenho entre países e cidades.
* Identificar oportunidades estratégicas (novos mercados, culinárias mais fortes, modelos de operação mais modernos).
* Avaliar diferenças de comportamento entre clientes e restaurantes.

A solução atende ao objetivo principal: **criar uma visão unificada dos KPIs do marketplace da Fome Zero**.

---

## 7. Próximos Passos

* Criar novas métricas mais avançadas (ex: clusterização de cidades, análise de sazonalidade aprofundada).
* Implementar novos filtros no dashboard.
* Adicionar mapas interativos com concentração de restaurantes.
* Desenvolver previsão de demanda por cidade.
* Criar comparativos temporais mais detalhados.

* Link https://arthurbarbosalima123-dot.github.io/portfolio_projetos/

---


