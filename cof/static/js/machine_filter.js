const apply = document.getElementById('apply_filters');
apply.addEventListener('click',applyFilters);

function applyFilters(){
    const product_type = document.getElementById('product_type').value.toString();
    const water_line_compitable = document.getElementById('water_line_compitable').value.toString();
    base = 'http://127.0.0.1:8000/machines_api.json?';

    if (product_type != "---"){
       var url =`${base}&product_type=${product_type}`;
    }
    if (water_line_compitable != "---"){
        var url =`${url}&water_line_compitable=${water_line_compitable}`;
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
        element.textContent = JSON.stringify(elem);
        data.appendChild(element);
      })
    
}

function onError(error){
    console.log(error); 
  }