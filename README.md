# AP1_ODS_SistemaDeRecomendacao  
**Cenário escolhido: Recomendação de Livros**  
Além de uma grande disponibilidade de dados e da variedade de features disponíveis para avaliar, o tema foi escolhido pela problemática atual: as pessoas estão parando de ler. Com o poder de LLMs resumirem longos textos, vídeos-resumos no Youtube, com o aumento do preço dos livros e com a falta de tempo do brasileiro médio, cada vez menos pessoas exercem a leitura. Isso poderia ser diferente se as pessoas tivessem certeza que gostariam do livro que lerão? Faria o preço valer a pena, ou se tornaria uma atividade prioritária no tempo livre? Neste intuito de trazer de volta um hábito perdido, faz-se importante um sistema eficaz de recomendação de livros.  
  
**Dataset utilizado: BX-Books e BX-Book_Ratings**  
from <https://github.com/MainakRepositor/Book-Recommender.git>  
  
**Tipo de similaridade: Cosseno**  
Rápida de calcular, bem estabelecida em sistemas de recomendação e fácil de interpretar. Ao final do teste, ao revelar a acurácia e investigar a esparsidade da matriz, foi considerado trocar para a Similaridade de Pearson, porém, ao avaliar com este método, não ouve melhora significativa (+0,01%) e o tempo de execução mais que dobrou. Prezando pela agilidade do código, e não havendo muita diferença, a Similaridade Cosseno foi mantida.  
  
**Explicação da lógica de recomendação**  
O sistema utiliza um modelo de recomendação colaborativa baseado em itens. Ele calcula a similaridade entre livros a partir das avaliações de usuários, utilizando similaridade cosseno para comparar os padrões de avaliação. Para gerar recomendações para um usuário, o sistema solicita o nome de um livro que o usuário gostou e sugere obras similares. A acurácia é avaliada verificando quantas dessas recomendações correspondem a livros que o usuário realmente gostou (avaliou com nota >= 7).  
  
**Resultado da acurácia: 26,17%**  
Total de recomendações = 1005  
Acertos = 278  
  
A baixa acurácia se dá provavelmente pela esparsidade da matriz de correlação (99,71%), ou seja, existem poucos usuários que avaliaram o mesmo livro. Com um dataset melhor, existe possibilidade de melhora na acurácia.
  
### Execução do Backend  
1. Em um terminal, digite cd backend
2. rode pip install -r requirements.txt
3. digite cd ..
4. execute com python -m uvicorn backend.main:app --reload  

### Execução do Frontend  
1. Em um terminal, digite cd frontend
2. rode pip install -r requirements.txt
3. digite cd ..
4. execute com python -m streamlit run frontend/app.py  

### Teste da acurácia
1. É necessário que vc já tenha instalado os requisitos do Backend
2. estando na pasta AP1_ODS, digite python avaliacao_acuracia.py