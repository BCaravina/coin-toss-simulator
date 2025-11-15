import time
import pandas as pd
import scipy.stats
import streamlit as st

# criando os session states para compilar as médias de cada lançamentos e criar um dataframe
if "experiment_no" not in st.session_state:
    st.session_state["experiment_no"] = 0

if "df_experiment_results" not in st.session_state:
    st.session_state["df_experiment_results"] = pd.DataFrame(
        columns=["no", "iterations", "mean"]
    )

st.header("Jogando uma moeda")

# criando função e gráfico que emulam os lançamentos da moeda e calcula suas médias
chart = st.line_chart([0.5])


def toss_coin(n):
    """Função que emula o lançamento de uma moeda n vezes e calcula sua média a cada novo lançamento."""
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean


# adicionando controle deslizante para selecionar a quantidade de tentativas
number_of_trials = st.slider("Número de tentativas?", 1, 1000, 10)
start_button = st.button("Executar")

if start_button:
    st.write(f"Executando o experimento de {number_of_trials} tentativas.")
    st.session_state["experiment_no"] += 1
    mean = toss_coin(number_of_trials)
    # adicionando a tabela de tentativas e médias à tela
    st.session_state["df_experiment_results"] = pd.concat(
        [
            st.session_state["df_experiment_results"],
            pd.DataFrame(
                data=[[st.session_state["experiment_no"], number_of_trials, mean]],
                columns=["no", "iterations", "mean"],
            ),
        ],
        axis=0,
    )
    st.session_state["df_experiment_results"] = st.session_state[
        "df_experiment_results"
    ].reset_index(drop=True)

st.write(st.session_state["df_experiment_results"])
