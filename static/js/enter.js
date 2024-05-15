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