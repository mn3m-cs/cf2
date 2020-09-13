const apply = document.getElementById('apply_filters');
apply.addEventListener('click',applyFilters);

function applyFilters(){
    const product_type= document.getElementById('product_type').value.toString();
    const flavor = document.getElementById('flavor').value.toString();
    const pack_size = document.getElementById('pack_size').value.toString();

    url = 'http://127.0.0.1:8000/pods_api.json?';

    if (product_type != "---"){
        url =`${url}&product_type=${product_type}`;
    }

    if (flavor != "---"){
        url =`${url}&flavor=${flavor}`;
     }

     if (pack_size != "---"){
        url =`${url}&pack_size=${pack_size}`;
     }
     console.log(url);
     fetch(url).then(onResponse).then(onJsonReady).catch(onError);

}

function onResponse(response){
    return response.json();
}
function onJsonReady(json){
    console.log(json);
    const data = document.getElementById('json_data');
    data.innerHTML='';
    const h1=document.createElement('h1');
    h1.textContent='products'
    data.appendChild(h1);
    json.forEach(elem =>{
        const element = document.createElement('p');
        //element.textContent =elem['name'];
        element.textContent = JSON.stringify(elem);
        data.appendChild(element);
      })
    
}

function onError(error){
    console.log(error); 
  }