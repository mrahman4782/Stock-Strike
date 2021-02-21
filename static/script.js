
function start() {
    const operval = document.querySelector('.oper')
    operval.innerHTML = "c"
}

function end() {

    const tiktxt = document.querySelector('#tableinput.row1');
    const pricetxt = document.querySelector('#tableinput.row2');
    const emtxt = document.querySelector('#tableinput.row3');
    const operval = document.querySelector('.oper')

    tiktxt.value = "";
    pricetxt.value = "";
    emtxt.value = "";

    operval.innerHTML = "h"
 
    
  
}