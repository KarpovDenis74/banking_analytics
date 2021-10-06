const currencyCard = document.querySelector('tbody');
const rateDate = document.querySelector('#cur__date');
const currencySelect = document.querySelector('#cur__select');
const api = new Api(apiUrl);

const cbEventInput = (elem) => {
    return api.getCurrencyList(elem.target.value).then(e => {
        if (e.results.length !== 0) {
            let temp = ' ';
            for (let i = 1; i <= e.results.length; i++) {
                temp = temp + `<tr>
                    <th scope="row">${i}</th>
                    <td>${e.results[i - 1].currency.num_code}</td>
                    <td>${e.results[i - 1].currency.char_code}</td>
                    <td>${e.results[i-1].nominal}</td>
                    <td>${e.results[i-1].currency.name}</td>
                    <td>${e.results[i-1].value} RUR</td>
                </tr>`;
            }
            currencyCard.innerHTML = temp;
        }
    })
        .catch(e => {
            currencyCard.innerHTML = `<tr>
                            <th scope="row">-</th>
                            <td>Нет данных по заданным параментрам</td>
                            <td></td>
                            <td></td>
                        </tr>`;
            console.log(e);
        })
};

const eventCurrencyInput = (elem) => {
    console.log(rateDate);
    console.log(rateDate.value);
    console.log(currencySelect);
    console.log(currencySelect.value);
    console.log(elem.target.value);
    return api.getCurrency(rateDate.value, elem.target.value);
};
const eventCurInput = debouncing(eventCurrencyInput, 1000);
// вешаем апи
currencySelect.addEventListener('change', eventCurInput);


const eventInput = debouncing(cbEventInput, 1000);
// вешаем апи
rateDate.addEventListener('input', eventInput);


// const counterId = document.querySelector('#counter');

// const ingredientsContainer = document.querySelector('.form__field-group-ingredientes-container');
// const nameIngredient = document.querySelector('#nameIngredient');
// const formDropdownItems = document.querySelector('.form__dropdown-items');
// const cantidadVal = document.querySelector('#cantidadVal');
// const cantidad = document.querySelector('#cantidad')
// const addIng = document.querySelector('#addIng');

// const api = new Api(apiUrl);
// const header = new Header(counterId);

// const defineInitialIndex = function () {
//     const ingredients = ingredientsContainer.querySelectorAll('.form__field-item-ingredient')
//     if (ingredients.length === 0) { return 1 }
//     const data = Array.from(ingredients).map(item => {
//         if (!item.getAttribute('id')) { return 0 }
//         if (!item.getAttribute('id').split('_')[1]) { return 0 }
//         return Number(item.getAttribute('id').split('_')[1])
//     })
//     data.sort((a, b) => a - b)
//     return data[data.length - 1] + 1
// }

// function Ingredients() {
//     let cur = defineInitialIndex();
//     // клик по элементам с сервера
//     const dropdown = (e) => {
//         if (e.target.classList.contains('form__item-list')) {
//             nameIngredient.value = e.target.textContent;
//             formDropdownItems.style.display = ''
//             cantidadVal.textContent = e.target.getAttribute('data-val');
//         }
//     };
//     // Добавление элемента из инпута
//     const addIngredient = (e) => {
//         if (nameIngredient.value && cantidad.value) {
//             const data = getValue();
//             const elem = document.createElement('div');
//             elem.classList.add('form__field-item-ingredient');
//             elem.id = `ing_${cur}`;
//             elem.innerHTML = `<span> ${data.name} ${data.value}${data.units}</span> <span class="form__field-item-delete"></span>
//                              <input id="nameIngredient_${cur}" name="nameIngredient_${cur}" type="hidden" value="${data.name}">
//                              <input id="valueIngredient_${cur}" name="valueIngredient_${cur}" type="hidden" value="${data.value}">
//                              <input id="unitsIngredient_${cur}" name="unitsIngredient_${cur}" type="hidden" value="${data.units}">`;
//             cur++;

//             ingredientsContainer.appendChild(elem);
//         }
//     };
//     // удаление элемента

//     const eventDelete = (e) => {
//         if (e.target.classList.contains('form__field-item-delete')) {
//             const item = e.target.closest('.form__field-item-ingredient');
//             item.removeEventListener('click', eventDelete);
//             item.remove()
//         };
//     };
//     ingredientsContainer.addEventListener('click', eventDelete);
//     // получение данных из инпутов для добавления
//     const getValue = (e) => {
//         const data = {
//             name: nameIngredient.value,
//             value: cantidad.value,
//             units: cantidadVal.textContent
//         };
//         clearValue(nameIngredient);
//         clearValue(cantidad);
//         return data;
//     };
//     // очистка инпута
//     const clearValue = (input) => {
//         input.value = '';
//     };
//     return {
//         clearValue,
//         getValue,
//         addIngredient,
//         dropdown
//     }
// }

// const cbEventInput = (elem) => {
//     return api.getIngredients(elem.target.value).then(e => {
//         if (e.length !== 0) {
//             const items = e.map(elem => {
//                 return `<a class="form__item-list" data-val="${elem.dimension}"">${elem.title}</a>`
//             }).join(' ')
//             formDropdownItems.style.display = 'flex';
//             formDropdownItems.innerHTML = items;
//         }
//     })
//         .catch(e => {
//             console.log(e)
//         })
// };

// const eventInput = debouncing(cbEventInput, 1000);

// // вешаем апи
// nameIngredient.addEventListener('input', eventInput);
// const ingredients = Ingredients();
// // вешаем слушатель на элементы с апи
// formDropdownItems.addEventListener('click', ingredients.dropdown);
// // вешаем слушатель на кнопку
// addIng.addEventListener('click', ingredients.addIngredient);
