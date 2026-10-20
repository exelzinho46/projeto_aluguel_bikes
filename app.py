import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Aluguel de Bicicletas",
    page_icon="🚲",
    layout="centered"
)

# Título
st.title("🚲 Aluguel de Bicicletas")
st.write("Escolha sua bicicleta e faça seu aluguel!")

st.divider()

# Nome do cliente
nome = st.text_input("👤 Nome do cliente")

# Escolha da bicicleta
bicicleta = st.selectbox(
    "🚲 Escolha sua bicicleta",
    [
        "Bicicleta comum",
        "Bicicleta elétrica",
        "Bicicleta infantil"
    ]
)

# Preços
if bicicleta == "Bicicleta comum":
    preco = 10
elif bicicleta == "Bicicleta elétrica":
    preco = 20
else:
    preco = 8

# Quantidade de horas
horas = st.number_input(
    "⏰ Quantas horas deseja alugar?",
    min_value=1,
    max_value=24,
    value=1
)

# Cálculo
total = preco * horas

st.divider()

# Resumo
st.subheader("📋 Resumo do aluguel")

coluna1, coluna2 = st.columns(2)

with coluna1:
    st.write("**Bicicleta:**")
    st.info(bicicleta)

with coluna2:
    st.write("**Preço por hora:**")
    st.info(f"R$ {preco:.2f}")

st.write(f"**Tempo de aluguel:** {horas} hora(s)")

st.metric(
    "💰 Valor total",
    f"R$ {total:.2f}"
)

st.divider()

# Botão
if st.button("🚲 Confirmar aluguel", use_container_width=True):

    if nome:
        st.success("✅ Aluguel realizado com sucesso!")

        st.write("### Dados do aluguel")
        st.write(f"👤 **Cliente:** {nome}")
        st.write(f"🚲 **Bicicleta:** {bicicleta}")
        st.write(f"⏰ **Tempo:** {horas} hora(s)")
        st.write(f"💰 **Total:** R$ {total:.2f}")

    else:
        st.warning("⚠️ Digite seu nome antes de confirmar o aluguel.")