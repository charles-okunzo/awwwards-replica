searchBtn = document.getElementById('search-btn');
form = document.getElementById('search-form');

searchBtn.onclick = ()=>{
    form.style.display = 'block'
    searchBtn.style.display = 'none'
}

// elements = document.querySelectorAll('div.project')

// $(()=>{
//     elements.forEach(element => {
//         $(element).hover(()=>{
//             $('.proj-content').slideToggle(500)
//         })
//     });
    
// })