<<<<<<< HEAD
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
=======
// Get the radio buttons
console.log("loaded")
const radioButtons = document.getElementsByName('radios');
const selectElement = document.getElementById('id_role');

// Add event listener to each radio button
radioButtons.forEach((radioButton) => {
  radioButton.addEventListener('change', (event) => {
    // Log the selected radio button's value
    selectElement.value = event.target.id;
  });
});

const radioNGO = document.getElementById("NGO");
  const radioVolunteer = document.getElementById("VOLUNTEER");
  const inputsNGO = document.querySelectorAll(".NGO");
  const inputsVolunteer = document.querySelectorAll(".Volunteer");
  const labelsNGO = document.querySelectorAll(".NGO");
  const labelsVolunteer = document.querySelectorAll(".Volunteer");
console.log(radioNGO)
  // Add an event listener to the radio buttons
  radioNGO.addEventListener("click", function() {
    // Hide the Volunteer inputs/labels
    inputsVolunteer.forEach(input => input.style.display= "none" );
    labelsVolunteer.forEach(label => label.style.display= "none");

    // Show the NGO inputs/labels
    inputsNGO.forEach(input => input.style.display= "inline");
    labelsNGO.forEach(label => label.style.display= "inline");
    const labelFirstName = document.querySelector("label[for='id_first_name']");
    if (labelFirstName) {
      labelFirstName.innerHTML = "Organization name:";
    }
  });

  radioVolunteer.addEventListener("click", function() {
    // Hide the NGO inputs/labels
    inputsNGO.forEach(input => input.style.display= "none");
    labelsNGO.forEach(label => label.style.display= "none");

    // Show the Volunteer inputs/labels
    inputsVolunteer.forEach(input => input.style.display= "inline");
    labelsVolunteer.forEach(label => label.style.display= "inline");

    const labelFirstName = document.querySelector("label[for='id_first_name']");
    if (labelFirstName) {
      labelFirstName.innerHTML = "First name:";
    }

  });
// const selectElement = document.getElementById('id_role');


>>>>>>> 8c4a4dd881a84bef01af66b8d969c69c51461fe7
