# AP1_ODS_SistemaDeRecomendacao  
Equipe:  
- Aline Daffiny Ferreira Gomes
- Leonardo Melo Crispim
- Mateus Bastos Magalhaes Mar  
  
## Relatório do sistema
**Cenário escolhido: Recomendação de Livros**  
Além de uma grande disponibilidade de dados e da variedade de features disponíveis para avaliar, o tema foi escolhido pela problemática atual: as pessoas estão parando de ler. Com o poder de LLMs resumirem longos textos, vídeos-resumos no Youtube, com o aumento do preço dos livros e com a falta de tempo do brasileiro médio, cada vez menos pessoas exercem a leitura. Isso poderia ser diferente se as pessoas tivessem certeza que gostariam do livro que lerão? Faria o preço valer a pena, ou se tornaria uma atividade prioritária no tempo livre? Neste intuito de incentivar e trazer de volta um hábito saudável perdido, faz-se importante um sistema eficaz de recomendação de livros.  
.  
.  
.  
**Dataset utilizado: BX-Books e BX-Book_Ratings**  
from <https://github.com/MainakRepositor/Book-Recommender.git>  
  
**Tipo de similaridade: Cosseno**  
Rápida de calcular, bem estabelecida em sistemas de recomendação, ideal para datasets esparsos e fácil de interpretar. Ao final do teste e ao revelar a acurácia, foi considerado trocar para a Similaridade de Pearson, porém, ao avaliar com este método, não ouve melhora significativa (+0,01%) e o tempo de execução mais que dobrou. Prezando pela otimização do código, e não havendo perda significativa de desempenho, a Similaridade Cosseno foi mantida.  
  
**Explicação da lógica de recomendação**  
O sistema utiliza um modelo de recomendação colaborativa baseado em itens. Ele calcula a similaridade entre livros a partir das avaliações de usuários, utilizando similaridade cosseno para comparar os padrões de avaliação. Para gerar recomendações para um usuário, o sistema solicita o nome de um livro que o usuário gostou e sugere obras similares. A acurácia é avaliada contabilizando recomendações únicas (dois livros podem gerar a mesma recomendação, mas ela será contabilizada somente uma vez) e verificando quantas dessas recomendações correspondem a livros que o usuário realmente gostou (avaliou com nota >= 6).  
.  
.  
.  
**Resultado da acurácia: 44,57%**  
O usuário selecionado possui 1029 avaliações, das quais foram dispostas 28% (288) para geração de recomendações e 72% (741) para servir de gabarito. O motivo de uma divisão tão específica é minimizar a diferenças entre o número de recomendações geradas e o número de exemplos disponíveis para o gabarito: se o modelo gera mais recomendações do que há disponível no gabarito para comparar, mesmo com um modelo perfeito, que sempre acerta, é impossível alcançar os 100% de acurácia.  
Total de recomendações únicas geradas = 718  
Acertos = 320  
Acc = acertos/total_recomendacoes = 320/718 = 0,44568 (aproximadamente 44,57%)  
  
A baixa acurácia se dá provavelmente pela precariedade do dataset de avaliações, com poucas pessoas avaliando o mesmo livro, com alguns livros com menos de 20 avaliações. Acredita-se que com um dataset melhor, existe possibilidade de melhora no desempenho.  
.  
.  
.  
.  
.  
## Manual de execução
### Execução do Backend  
1. Em um terminal, digite `cd backend`
2. rode `pip install -r requirements.txt`
3. digite `cd ..`
4. execute com `python -m uvicorn backend.main:app --reload`  

### Execução do Frontend  
1. Em um terminal, digite `cd frontend`
2. rode `pip install -r requirements.txt`
3. digite `cd ..`
4. execute com `python -m streamlit run frontend/app.py`  

### Teste da acurácia
1. Se os requisitos do Backend já foram instalados, siga para o passo 4. Do contrário, em um terminal, digite `cd backend`
2. rode `pip install -r requirements.txt`
3. digite `cd ..`
4. estando na pasta AP1_ODS, digite `python avaliacao_acuracia.py`
