import sqlite3

from typing import Optional, Text

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class cliente(BaseModel):
    cpf : str
    nome : str
    email : str
    valor : int

def excluir_registro(cpf : str):
    c=sqlite3.connect('/Users/Ijovem03/coursepython/database/tatoo.db')
    cr=c.cursor()
    cr.execute("""  delete from clientes where cpf = ?   """, (cpf,))
    c.commit()
    c.close()
    return 0

def score():
    c=sqlite3.connect('/Users/Ijovem03/coursepython/database/tatoo.db')
    cr=c.cursor()
    cr.execute("""select cpf , nome , email , sum(valor) from clientes group by cpf, nome, email""")
    lista=cr.fetchall()
    c.close()
    return (lista)

@app.post("/gravar")
def gravar(c: cliente):
    msg= " gracias sr/sra o seu cpf esta invalido: "  + c.nome + " cpf: "   + c.cpf
    return {"msg": msg}
    
@app.put("/atualizar")
def atualizar(C: cliente):
    msg= " ola sr/sra seus dados foram atualizados! " + c.nome + " cpf " + c.cpf 
    return {"msg": msg}

@app.delete("/excluir")
def excluir(cpf : str): 
    excluir_registro(cpf) 
    return 0

@app.get("/listar_clientes")
def listar_clientes():
    return {"Hello": "World"}

@app.get("/listar_score")
def listar_score():
    return score()

@app.get("/listar_unico")
def listar_unico():
    return {"Hello": "World"}