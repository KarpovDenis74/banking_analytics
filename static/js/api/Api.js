
class Api {
    constructor(apiUrl) {
        this.apiUrl =  apiUrl;
    }
  getCurrencyList(id) {
    return fetch(`${this.apiUrl}currency/${id}/`, {
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
  }

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
