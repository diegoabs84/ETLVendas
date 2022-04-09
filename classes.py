from ast import Num
from numbers import Number
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, VARCHAR, CHAR, NUMERIC, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.ext.declarative import declarative_base
import conexao




Base = declarative_base()

#Declarando bases para referência das tabelas do banco de dados operacional

class Clientes():
    def __init__(self,cod_cli, lim_credito, sld_devedor, nom_cli, fones) -> None:
        self.cod_cli = cod_cli
        self.lim_credito = lim_credito
        self.sld_devedor = sld_devedor
        self.nom_cli = nom_cli
        self.fones = fones
    
    
class Fornecedores():
    def __init__(self,cod_forn,uf_forn,sld_credor,nom_forn) -> None:
        self.cod_forn = cod_forn
        self.uf_forn = uf_forn
        self.sld_creddor = sld_credor
        self.nom_forn = nom_forn


class Pedidos():
    def __init__(self,num_ped,cod_cli,dat_ped,sta_pedido,val_ped,val_a_vista,val_a_prazo,sld_devedor) -> None:
        self.num_ped = num_ped
        self.cod_cli = cod_cli
        self.dat_ped = dat_ped
        self.sta_pedido = sta_pedido
        self.val_ped = val_ped
        self.val_a_vista = val_a_vista
        self.val_a_prazo = val_a_prazo
        self.sld_devedor = sld_devedor


class Parcelas():
    def __init__(self,num_ped,dat_venc,val_parc,parc_paga) -> None:
        self.num_ped = num_ped
        self.dat_venc = dat_venc
        self.val_parc = val_parc
        self.parc_paga = parc_paga


class Produtos():
    def __init__(self,cod_prod,qtd_estoque,per_parc,preco_pro,cod_forn,dsc_prod) -> None:
        self.cod_prod = cod_prod
        self.qtd_estoque = qtd_estoque
        self.per_parc = per_parc
        self.preco_pro = preco_pro
        self.cod_forn = cod_forn
        self.dsc_prod = dsc_prod


class Tempo():
    def __init__(self, dat_nota) -> None:
        self.dat_nota = dat_nota


class ItensNota():
    def __init__(self,num_nota,cod_prod,qtd_ped,preo_pro) -> None:
        self.num_nota = num_nota
        self.cod_prod = cod_prod
        self.qtd_ped = qtd_ped
        self.preo_pro = preo_pro

class ItensPedido():
    def __init__(self,num_ped,cod_prod,qtd_ped,preco_pro) -> None:
        self.num_ped = num_ped
        self.cod_prod = cod_prod
        self.qtd_ped = qtd_ped
        self.preco_pro = preco_pro



#Declarando bases para referência das tabelas do banco de dados dimensional

class Dim_cliente():
    def __init__(self,id_cliente,nome_cliente,cidade_cli,uf_cli) -> None:
        self.id_cliente = id_cliente
        self.nome_cliente = nome_cliente
        self.cidade_cli = cidade_cli
        self.uf_cli = uf_cli

    
class Dim_fornecedores():
    def __init__(self,id_forn,nom_forn,regiao_forn) -> None:
        self.id_forn = id_forn
        self.nom_forn = nom_forn
        self.regiao_forn = regiao_forn

    
class Dim_produtos():
    def __init__(self,id_prod,dsc_prod,classe_prod) -> None:
        self.id_prod = id_prod
        self.dsc_prod = dsc_prod
        self.classe_prod = classe_prod


class Dim_tiposVendas():
    def __init__(self,id_tipo_venda,desc_tipo_venda) -> None:
        self.id_tipo_venda = id_tipo_venda
        self.desc_tipo_venda =desc_tipo_venda
        

class Dim_tempo():
    def __init__(self,id_tempo,nu_ano,nu_mes,nu_anomes,sg_mes,nm_mesano,nm_mes,nu_dia) -> None:
        self.id_tempo = id_tempo
        self.nu_ano = nu_ano
        self.nu_mes = nu_mes
        self.nu_anomes = nu_anomes
        self.sg_mes = sg_mes
        self.nm_mesano = nm_mesano
        self.nm_mes = nm_mes
        self.nu_dia = nu_dia


class Ft_vendas():
    def __init__(self,id_prod,id_tempo,id_tipo_venda,id_forn,val_renda) -> None:
        self.id_prod = id_prod
        self.id_tempo = id_tempo
        self.id_tipo_venda = id_tipo_venda
        self.id_forn = id_forn
        self.valor_renda - val_renda


class Ft_impontualidade():
    def __init__(self,id_temp,id_cliente,valor_parc_atrasadas,valor_parc_total) -> None:
        self.id_tempo = id_temp
        self.id_cliente = id_cliente
        self.valor_parc_atrasadas = valor_parc_atrasadas
        self.valor_parc_total = valor_parc_total
        
