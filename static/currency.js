const currencyCard = document.querySelector('tbody');
const rateDate = document.querySelector('#cur__date');
const currencyList = document.getElementById('cur_list');
const curList = currencyList.getElementsByTagName('input');
const api = new Api(apiUrl);

const cbEventSelect = (elem) => {
    var select = "currency=";
    for (var i = 0; i < curList.length; i++) {
        if (curList[i].checked) {
            select += curList[i].value + ",";
        };
    };
    if (select == "currency=") {
        select = null
    }
    else {
        select = select.slice(0, -1);
    };
    console.log(select);
    return api.getCurrencyList(date = rateDate.value, num_code = select).then(e => {
        non_data = `<tr>
                        <th scope="row">-</th>
                        <td>Нет данных по заданным параметрам</td>
                        <td></td>
                        <td></td>
                    </tr>`;
        if (e.results.length !== 0) {
            console.log(`e.results.length = ${e.results.length}`);
            let temp = ' ';
            for (let i = 1; i <= e.results.length; i++) {
                temp = temp + `<tr>
                    <th scope="row">${i}</th>
                    <td>${e.results[i - 1].currency.num_code}</td>
                    <td>${e.results[i - 1].currency.char_code}</td>
                    <td>${e.results[i - 1].nominal}</td>
                    <td>${e.results[i - 1].currency.name}</td>
                    <td>${e.results[i - 1].value} RUR</td>
                </tr>`;
            }
            currencyCard.innerHTML = temp;
        } else {
            currencyCard.innerHTML = non_data;
            console.log(e);
        };
    })
        .catch(e => {
            currencyCard.innerHTML = non_data;
            console.log(e);
        })
};

const eventSelect = debouncing(cbEventSelect, 1000);
currencyList.addEventListener('click', eventSelect)
rateDate.addEventListener('input', eventSelect);