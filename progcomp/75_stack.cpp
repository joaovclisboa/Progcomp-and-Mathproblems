class Solution {
public:
    std::vector<int> asteroidCollision(std::vector<int>& asteroids){
    std::vector<int> pilha;
    for (int ast : asteroids){
        bool ast_destruido = false;
        //nos iremos fazer a comparação em se os 3 casos forem verdadeiros:
        //a pilha esta nao vazia
        //o topo da pilha é um elemento positivo
        //o elemento sendo analisado atualmente é negativo
        while (ast < 0 && !pilha.empty() && pilha.back() > 0){
            if (std::abs(ast) == pilha.back()){
                pilha.pop_back();
                ast_destruido = true;
                break;
            }
            else if(pilha.back() > std::abs(ast)){
                ast_destruido = true;
                break;
            }
            else{
                pilha.pop_back();
            }
        }
        if (!ast_destruido){
            pilha.push_back(ast);
        }
    }
    return pilha;
}
};
