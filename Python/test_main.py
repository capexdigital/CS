import pytest

from Exerc_1 import desconto, total_sem_desconto, total_com_desconto
from Exerc_2 import preco_unitario, calcular_valor_pedido, descricao_pedido
from Exerc_3 import calcular_valor_base, aplicar_desconto, aplicar_adicional, calcular_total
from Exerc_4 import cadastrar_livro, buscar_por_id, buscar_por_autor, remover_livro, resetar


# ---------------------------------------------------------------------------
# Exerc_1 - Loja (desconto por valor)
# ---------------------------------------------------------------------------

class TestExerc1:
    def test_sem_desconto(self):
        assert desconto(2000) == 2000

    def test_limite_2500_sem_desconto(self):
        assert desconto(2500) == 2500

    def test_desconto_4_porcento(self):
        assert desconto(3000) == pytest.approx(3000 * 0.96)

    def test_limite_6000_muda_faixa(self):
        assert desconto(6000) == pytest.approx(6000 * 0.93)

    def test_desconto_7_porcento(self):
        assert desconto(7000) == pytest.approx(7000 * 0.93)

    def test_limite_10000_muda_faixa(self):
        assert desconto(10000) == pytest.approx(10000 * 0.89)

    def test_desconto_11_porcento(self):
        assert desconto(15000) == pytest.approx(15000 * 0.89)

# ---------------------------------------------------------------------------
# Exerc_2 - Loja de gelados (sabor/tamanho)
# ---------------------------------------------------------------------------

class TestExerc2:
    def test_preco_acai_pequeno(self):
        assert preco_unitario('ac', 'p') == 11

    def test_preco_acai_medio(self):
        assert preco_unitario('ac', 'm') == 16

    def test_preco_acai_grande(self):
        assert preco_unitario('ac', 'g') == 20

    def test_preco_cupuacu_pequeno(self):
        assert preco_unitario('cp', 'p') == 9

    def test_preco_cupuacu_medio(self):
        assert preco_unitario('cp', 'm') == 14

    def test_preco_cupuacu_grande(self):
        assert preco_unitario('cp', 'g') == 18

    def test_preco_case_insensitive(self):
        assert preco_unitario('AC', 'P') == 11

    def test_preco_invalido(self):
        assert preco_unitario('xx', 'p') is None

    def test_calcular_valor_pedido(self):
        assert calcular_valor_pedido('ac', 'm', 3) == 48

    def test_calcular_valor_pedido_invalido(self):
        with pytest.raises(ValueError):
            calcular_valor_pedido('xx', 'p', 1)

    def test_descricao_pedido(self):
        assert descricao_pedido('cp', 'g') == 'Cupuaçu Grande'

    def test_descricao_pedido_invalida(self):
        with pytest.raises(ValueError):
            descricao_pedido('xx', 'p')


# ---------------------------------------------------------------------------
# Exerc_3 - Copiadora (serviço, desconto por página, adicional)
# ---------------------------------------------------------------------------

class TestExerc3:
    def test_valor_base_digitalizacao(self):
        assert calcular_valor_base(1, 100) == pytest.approx(110)

    def test_valor_base_impressao_colorida(self):
        assert calcular_valor_base(2, 100) == pytest.approx(100)

    def test_valor_base_impressao_pb(self):
        assert calcular_valor_base(3, 100) == pytest.approx(40)

    def test_valor_base_fotocopia(self):
        assert calcular_valor_base(4, 100) == pytest.approx(20)

    def test_valor_base_servico_invalido(self):
        with pytest.raises(ValueError):
            calcular_valor_base(9, 100)

    def test_sem_desconto_abaixo_de_20(self):
        assert aplicar_desconto(100, 10) == 100

    def test_desconto_15_porcento(self):
        assert aplicar_desconto(100, 50) == pytest.approx(85)

    def test_desconto_20_porcento(self):
        assert aplicar_desconto(100, 500) == pytest.approx(80)

    def test_desconto_25_porcento(self):
        assert aplicar_desconto(100, 5000) == pytest.approx(75)

    def test_adicional_zero(self):
        assert aplicar_adicional(100, 0) == 100

    def test_adicional_encadernacao_simples(self):
        assert aplicar_adicional(100, 1) == 115

    def test_adicional_encadernacao_capa_dura(self):
        assert aplicar_adicional(100, 2) == 140

    def test_adicional_invalido(self):
        with pytest.raises(ValueError):
            aplicar_adicional(100, 9)

    def test_calcular_total_completo(self):
        # 100 páginas de impressão colorida = 100, desconto 15% = 85, + encadernação simples = 100
        assert calcular_total(2, 100, 1) == pytest.approx(100)


# ---------------------------------------------------------------------------
# Exerc_4 - Cadastro de livros
# ---------------------------------------------------------------------------

class TestExerc4:
    @pytest.fixture(autouse=True)
    def limpar_lista(self):
        resetar()
        yield
        resetar()

    def test_cadastrar_livro_gera_id_incremental(self):
        livro1 = cadastrar_livro('Dom Casmurro', 'Machado de Assis', 'Editora A')
        livro2 = cadastrar_livro('Memórias Póstumas', 'Machado de Assis', 'Editora A')
        assert livro1['id'] == 1
        assert livro2['id'] == 2

    def test_buscar_por_id_encontrado(self):
        cadastrar_livro('1984', 'George Orwell', 'Editora B')
        livro = buscar_por_id(1)
        assert livro['nome'] == '1984'

    def test_buscar_por_id_nao_encontrado(self):
        assert buscar_por_id(999) is None

    def test_buscar_por_autor_parcial(self):
        cadastrar_livro('Dom Casmurro', 'Machado de Assis', 'Editora A')
        resultados = buscar_por_autor('machado')
        assert len(resultados) == 1
        assert resultados[0]['nome'] == 'Dom Casmurro'

    def test_buscar_por_autor_nao_encontrado(self):
        cadastrar_livro('1984', 'George Orwell', 'Editora B')
        assert buscar_por_autor('Machado') == []

    def test_remover_livro_existente(self):
        cadastrar_livro('1984', 'George Orwell', 'Editora B')
        assert remover_livro(1) is True
        assert buscar_por_id(1) is None

    def test_remover_livro_inexistente(self):
        assert remover_livro(999) is False