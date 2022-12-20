### Formatação no terminal


<pre>
    <code>
        nome = input('Qual é o seu nome? ')
        print(f'Prazer em te conhecer, {nome:>20}')  /* usará 20 caracteres */
            /*    usando :> alinha à direita, :< à esquerda e ^ centraliza. */
            /*    usando :=^20 centraliza a palavra e cerca com = (ou qualquer outro caractere)  
            */  
        # imprimir números fracionados: {n:.1f} exibe 1 casa decimal, {n:.0f} exibe nenhuma casa.

        # para não quebrar linha: no final da função print, inclua: end = ''
        quebrar linha: \n   
    </code>
</pre>