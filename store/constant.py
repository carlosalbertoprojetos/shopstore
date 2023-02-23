from django.urls import reverse_lazy as _


STATE_CHOICES = (
		('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'),
		('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'),
		('MG','MG'), ('PA','PA'), ('PB','PB'), ('PE','PE'), ('PI','PI'), ('PR','PR'),
		('RJ','RJ'), ('RN','RN'), ('RO','RO'), ('RR','RR'), ('RS','RS'), ('SC','SC'),
		('SE','SE'), ('SP','SP'), ('TO','TO'),    
    )

TYPE = (
    ('Compra', 'compra'),
    ('Venda', 'venda'),
    ('Outros', 'outros')
)
   
STATUS_CHOICES = (
    ('Pendente', 'pendente'),
    ('Aguardando', 'aguardando'),
    ('Entregue', 'entregue'),
    ('Cancelado', 'cancelado'),
)

STATUS_PARCELA_CHOICES = (
    ('Sim', 'Sim'),
    ('Não', 'Não'),    
)


PGTO_CHOICES = (
    ("Boleto", "Boleto"),
    ("Cheque", "Cheque"),
    ("C/Entrega", "C/Entrega"),
    ("Pix", "Pix"),
    ("Cartão", "Cartão"),
    ("Dinheiro", "Dinheiro"),
)

SEXO_CHOICES = (
    ('M','M'), ('F','F'), ('OUTRO','OUTRO'), ('PREFIRO NÃO DIZER','PREFIRO NÃO DIZER'),
)

RACA_CHOICES = (
    ('BRANCA','BRANCA'), ('PRETA','PRETA'), ('PARDA','PARDA'), ('AMARELA','AMARELA'), ('INDÍGENA','INDÍGENA'),
)

CONTA_STATUS_CHOICES = (
    ('a', 'A Pagar'),
    ('p', 'Pago'),
)

TYPE_CHOICES = [
    ('credit','Credit'),
    ('debit','Debit'),
]

MOVIMENT_CHOICES = (
    ('e', 'entrance'),
    ('x', 'exit'),
)

OPERATION_TYPE = (
    ('buy', 'Buy'),
    ('sell', 'Sell'),
)
