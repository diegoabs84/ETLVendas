from classes import (Clientes, Fornecedores, Pedidos, Parcelas, Produtos, Tempo, ItensNota, ItensPedido, Dim_cliente, Dim_fornecedores, Dim_produtos, Dim_tempo, Dim_tiposVendas, Base)
from conexao import (session)
from inspect import Traceback

#Extração dos dados do modelo operacional

def ext_op():

    try:
        vendas_dict = {
            "clientes" : [i for i in session.query(Clientes).all()],
            "fornecedores" : [i for i in session.query(Fornecedores).all()],
            "pedidos" : [i for i in session.query(Pedidos).all()],
            "parcelas" : [i for i in session.query(Parcelas).all()],
            "produtos" : [i for i in session.query(Produtos).all()],
            "tempo" : [i for i in session.query(Tempo).all()],
            "itensNota" : [i for i in session.query(ItensNota).all()],
            "itensPedido" : [i for i in session.query(ItensPedido).all()],


        }
    except Exception as e:
        Traceback(e)
    
    return vendas_dict

#Processo de alteração e preenchimento dos dados

def tl_dim_vendas(vendas : dict):

    dim_vendas = { "dm_clientes" : [], "dm_fornecedor" : [], "dm_produto" : [], "dm_tempo" : [], "dm_tiposVendas" : [], "ft_vendas" : [], "ft_impontualidade" : []}


    try:
        #Preparando para preencher a tabela dimensional cliente
        count = 0
        for a in vendas["clientes"]:
            count+=1
            cli = Dim_cliente(a,count)
            dim_vendas["dm_clientes"].append(cli.id_cliente, cli.nome_cliente, "Aracaju", "SE")
            session.add(cli)

        #Preparando para preencher a tabela dimensional fornecedores
        count = 0
        for a in vendas["fornecedores"]:
            count+=1
            forn = Dim_fornecedores(a,count)
            dim_vendas["dm_fornecedor"].append(count,forn.id_forn, forn.regiao_forn)
            session.add(forn)
        
        #Preparando para preencher a tabela dimensional produtos
        count = 0
        for a in vendas["produtos"]:
            count+=1
            prod = Dim_produtos(a,count)
            dim_vendas["dm_produto"].append(prod.id_prod, prod.dsc_prod, "Teste")
            session.add(prod)
        
        #Preparando para preencher a tabela dimensional produtos
        count = 0
        for a in vendas["produtos"]:
            count+=1
            prod = Dim_produtos(a,count)
            dim_vendas["dm_produto"].append(prod.id_prod, prod.dsc_prod, "Teste")
            session.add(prod)
        

    except Exception as e:
        Traceback(e)    

        session.commit()
        

def main():
     vend = ext_op()
     tl_dim_vendas(vend)

if __name__ == '__main__':
     main()
     
     

    