let searchBtn = document.getElementById('search-btn');
let form = document.getElementById('search-form');
let logo = document.getElementById('awwwards-logo')

searchBtn.onclick = ()=>{
    form.style.display = 'block'
    searchBtn.style.display = 'none'
    logo.style.display = 'none'
}

// elements = document.querySelectorAll('div.project')

// $(()=>{
//     elements.forEach(element => {
//         $(element).hover(()=>{
//             $('.proj-content').slideToggle(500)
//         })
//     });
    
// })