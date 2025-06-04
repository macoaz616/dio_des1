# dio_des1
📚 Documentação da API
get_card_brand(card_number)
Detecta a bandeira do cartão baseada no número.
Parâmetros:

card_number (str): Número do cartão (pode incluir espaços e hífens)

Retorna:

str: Nome da bandeira ou "Unknown or unsupported brand"

validate_card_number(card_number)
Valida o número do cartão usando o algoritmo de Luhn.
Parâmetros:

card_number (str): Número do cartão

Retorna:

bool: True se válido, False caso contrário

get_card_info(card_number)
Retorna informações completas sobre o cartão.
Parâmetros:

card_number (str): Número do cartão

Retorna:

dict: Dicionário com as chaves:

brand: Bandeira do cartão
is_valid: Se é válido pelo algoritmo de Luhn
cleaned_number: Número limpo (apenas dígitos)
length: Comprimento do número



🧪 Exemplos de Teste
python# Números de teste (não são cartões reais)
test_cards = [
    "4532 1234 5678 9012",  # Visa
    "5555-5555-5555-4444",  # MasterCard  
    "3782 822463 10005",    # American Express
    "6011 1111 1111 1117",  # Discover
    "3056 9309 0259 04",    # Diners Club
    "invalid",              # Inválido
    "",                     # Vazio
]

for card in test_cards:
    info = get_card_info(card)
    print(f"Cartão: {card}")
    print(f"  Bandeira: {info['brand']}")
    print(f"  Válido: {info['is_valid']}")
    print(f"  Comprimento: {info['length']}")
    print()
⚠️ Importante

Segurança: Esta biblioteca apenas identifica bandeiras e valida formato. Para processamento real de pagamentos, use sempre gateways de pagamento seguros e certificados PCI-DSS.
Números de Teste: Os exemplos usam números de teste que não representam cartões reais.
Privacidade: Nunca armazene números de cartão completos em logs ou bases de dados não criptografadas.

🔒 Algoritmo de Luhn
O algoritmo de Luhn é usado para validar números de cartão de crédito:

Começando pelo dígito mais à direita (excluindo o dígito verificador)
Dobramos cada segundo dígito
Se o resultado for maior que 9, subtraímos 9
Somamos todos os dígitos
Se a soma for divisível por 10, o número é válido

🛠️ Tratamento de Erros
A biblioteca trata os seguintes casos de erro:

Entrada inválida: Retorna "Invalid input" para entradas None ou não-string
Comprimento inválido: Retorna "Invalid card number length" para números muito curtos/longos
Formato inválido: Retorna "Unknown or unsupported brand" para números não reconhecidos

📝 Licença
Este código é fornecido como exemplo educacional. Use por sua própria conta e risco em aplicações de produção.
🤝 Contribuições
Para melhorar este código:

Adicione suporte para novas bandeiras de cartão
Melhore os padrões regex existentes
Adicione mais casos de teste
Melhore a documentação
