# Diagnóstico PR #133 — execução do login full-screen

Arquivo temporário de evidência para o ciclo TDD do diagnóstico. A hipótese testada é que a marca visual está sendo renderizada como efeito colateral do import de `services.ui`, portanto somente no primeiro carregamento do módulo Python e não em cada rerun/sessão do Streamlit.
