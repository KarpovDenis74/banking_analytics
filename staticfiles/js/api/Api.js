
class Api {
    constructor(apiUrl) {
        this.apiUrl =  apiUrl;
    }
  getCurrencyList(date = null, num_code = null) {
    var tmp = "?";
    if (date !== null) {
      tmp += `date=${date}&`
    };
    if (num_code == null || String(num_code).length < 1) {
      tmp += ` `;
    } else  {
      tmp += num_code;
    };
    return fetch(`${this.apiUrl}currency/${tmp}`, {
      headers: {
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
        'Content-Type': 'application/json'
      }
    })
      .then(e => {
        if (e.ok) {
          return e.json()
        }
        return Promise.reject(e.statusText)
      })
  };

  // getPurchases () {
  //   return fetch(`${this.apiUrl}purchases/${id}/`, {
  //     headers: {
  //       'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
  //       'Content-Type': 'application/json'
  //     }
  //   })
  //     .then( e => {
  //         if(e.ok) {
  //             return e.json()
  //         }
  //         return Promise.reject(e.statusText)
  //     })
  // }
  // addPurchases (id) {
  //   return fetch(`${this.apiUrl}purchases/${id}/`, {
  //     method: 'POST',
  //     headers: {
  //       'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
  //       'Content-Type': 'application/json'
  //     },
  //     body: JSON.stringify({
  //       id: id
  //     })
  //   })
  //     .then( e => {
  //         if(e.ok) {
  //             return e.json()
  //         }
  //         return Promise.reject(e.statusText)
  //     })
  // }
  // removePurchases (id){
  //   return fetch(`${this.apiUrl}purchases/${id}/`, {
  //     method: 'DELETE',
  //     headers: {
  //       'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
  //       'Content-Type': 'application/json'
  //     }
  //   })
  //     .then( e => {
  //         if(e.ok) {
  //             return e.json()
  //         }
  //         return Promise.reject(e.statusText)
  //     })
  // }
  // addSubscriptions(id) {
  //   return fetch(`${this.apiUrl}subscriptions/${id}/`, {
  //     method: 'POST',
  //     headers: {
  //       'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
  //       'Content-Type': 'application/json'
  //     },
  //     body: JSON.stringify({
  //       id: id
  //     })
  //   })
  //     .then( e => {
  //         if(e.ok) {
  //             return e.json()
  //         }
  //         return Promise.reject(e.statusText)
  //     })
  // }
  // removeSubscriptions (id) {
  //   return fetch(`${this.apiUrl}subscriptions/${id}/`, {
  //     method: 'DELETE',
  //     headers: {
  //       'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
  //       'Content-Type': 'application/json'
  //     }
  //   })
  //     .then( e => {
  //         if(e.ok) {
  //             return e.json()
  //         }
  //         return Promise.reject(e.statusText)
  //     })
  // }
  // addFavorites (id)  {
  //   return fetch(`${this.apiUrl}favorites/${id}/`, {
  //     method: 'POST',
  //     headers: {
  //       'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
  //       'Content-Type': 'application/json'
  //     },
  //     body: JSON.stringify({
  //       id: id
  //     })
  //   })
  //       .then( e => {
  //           if(e.ok) {
  //               return e.json()
  //           }
  //           return Promise.reject(e.statusText)
  //       })
  // }
  // removeFavorites (id) {
  //   return fetch(`${this.apiUrl}favorites/${id}/`, {
  //     method: 'DELETE',
  //     headers: {
  //       'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
  //       'Content-Type': 'application/json'
  //     }
  //   })
  //       .then( e => {
  //           if(e.ok) {
  //               return e.json()
  //           }
  //           return Promise.reject(e.statusText)
  //       })
  // }
  //   getIngredients  (text)  {
  //     return fetch(`${this.apiUrl}ingredients/?query=${text}`, {
  //       headers: {
  //               'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
  //               'Content-Type': 'application/json'
  //           }
  //       })
  //           .then( e => {
  //               if(e.ok) {
  //                   return e.json()
  //               }
  //               return Promise.reject(e.statusText)
  //           })
  //   }
}
