    // Função para fazer a solicitação AJAX e preencher os campos de Endereço, Bairro e Cidade
    function preencherEndereco(cep) {
        // Substitua 'sua-api-de-cep' pela URL da sua API de consulta de CEP
        const apiUrl = `https://viacep.com.br/ws/${cep}/json`;
    
        // Fazer solicitação AJAX
        $.getJSON(apiUrl, function(data) {
          // Verificar se os dados foram retornados com sucesso
          if (!("erro" in data)) {
            // Preencher os campos com os dados retornados
            document.getElementById("address").value = data.logradouro;
            document.getElementById("bairro").value = data.bairro;
            document.getElementById("cidade").value = data.localidade;
          } else {
            alert("CEP não encontrado.");
          }
        });
      }
    
      // Adicionar evento de mudança para o campo de CEP
      document.getElementById("cep").addEventListener("change", function() {
        // Obter o valor do CEP
        const cep = this.value.replace(/\D/g, '');
    
        // Chamar a função para preencher os campos
        preencherEndereco(cep);
      });
  
     document.getElementById('vacancies').addEventListener('input', function(e) {

      this.value = this.value.replace(/[^0-9.]/g, '');
    
    });
    document.addEventListener('DOMContentLoaded', function() {

          
      const inputs = document.querySelectorAll('input:not([type="radio"]), select, button');
    
        inputs.forEach(input => {
    
        input.addEventListener('keydown', function(event) {
    
            if (event.key === 'Enter') {
    
              
            event.preventDefault();
      
         
    
            const index = Array.from(inputs).indexOf(event.target);
    
                  
            const nextIndex = (index + 1) % inputs.length;
    
  
             const nextInput = inputs[nextIndex];
    
            nextInput.focus();
   
            if (nextInput.tagName === 'BUTTON') {
    
              nextInput.click();
    
            }
    
          }
    
        });
    
      });
    
    });






    // Função para verificar se os botões de rádio foram marcados
function checkRadioButtons() {
  const radioButtons = document.querySelectorAll('input[name="price-type"]');
  for (const rb of radioButtons) {
    if (rb.checked) {
      return true;
    }
  }
  return false;
}

// Adiciona o event listener para o evento 'keydown' no documento
document.addEventListener('DOMContentLoaded', function() {
  const inputs = document.querySelectorAll('input:not([type="radio"]), select, button');

  inputs.forEach(input => {
    input.addEventListener('keydown', function(event) {
      if (event.key === 'Enter') {
        event.preventDefault();
        const index = Array.from(inputs).indexOf(event.target);
        const nextIndex = (index + 1) % inputs.length;
        const nextInput = inputs[nextIndex];

        if (nextInput.tagName === 'BUTTON') {
          // Verifica se os botões de rádio foram marcados antes de submeter o formulário
          if (!checkRadioButtons()) {
            alert('Por favor, selecione uma forma de cobrança.');
            return; // Impede a submissão do formulário
          }
          nextInput.click();
        } else {
          nextInput.focus();
        }
      }
    });
  });
});

// Adiciona o event listener para o botão de submit
document.getElementById('submit-btn').addEventListener('click', function(event) {
  if (!checkRadioButtons()) {
    alert('Por favor, selecione uma forma de cobrança.');
    event.preventDefault();
  }
});