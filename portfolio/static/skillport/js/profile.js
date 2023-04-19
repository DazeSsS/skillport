console.log("привет")
const label = document.querySelector('#login')
const input = document.createElement('input')
const login = document.querySelector('#log_button')
const createElement = document.createElement('label')
function doInput()
    { 
    label.innerHTML = ''
    label.append(input)
    } 
function doLabel()
    {
    input.remove()
    }
login.addEventListener('click', doInput)
login.addEventListener('dblclick', doLabel)
console.log(login)