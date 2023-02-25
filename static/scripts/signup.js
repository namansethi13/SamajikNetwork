const radioButtons = document.querySelectorAll('input[name="user"]');
let form= document.querySelector('form')
radioButtons.forEach(rdbtn => {
    rdbtn.addEventListener("click",()=>{
        let value=String(rdbtn.attributes[3].value);
        if(value=="volunteer")
        {
            vform();
            return;
        }
        oform();
        
    })
});


function vform() {
    let vform =document.querySelector('.login100-form');
    let oform =document.querySelector('.oform');
    oform.classList.add('hidden')
    vform.classList.remove('hidden')
    return;
}

function oform(){
    let vform =document.querySelector('.login100-form');
    let oform =document.querySelector('.oform')
    oform.classList.remove('hidden')
    vform.classList.add('hidden')
    return;
} 