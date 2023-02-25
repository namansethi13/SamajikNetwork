const radioButtons = document.querySelectorAll('#id_role');
let form= document.querySelector('form')
radioButtons.forEach(rdbtn => {
    rdbtn.addEventListener("click",()=>{
        let value=String(radioButtons[0].selectedOptions[0].value);

        // print(value)
        if(value=="VOLUNTEER")
        {
            console.log("on")
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