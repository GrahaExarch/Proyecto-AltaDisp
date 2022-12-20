export default ($axios)=>({
  getCurrencyUSD(){return $axios.$get('currency/get/usd')},
  getCurrencyUF(){return $axios.$get('currency/get/uf')},
  getWeather(){return $axios.$get('weather/get')},
})
