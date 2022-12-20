import api from '@/services/api.js'

function initialState() {
  return {
  }}

const state = () => initialState()

const actions = {

  async getCurrencyUSD({commit},params){
    try{
      const response = await api(this.$axios).getCurrencyUSD()
      if (response.status){
        return response.currency
      }
      return false
    } catch(error){
      return false
    }
  },
  async getCurrencyUF({commit},params){
    try{
      const response = await api(this.$axios).getCurrencyUF()
      if (response.status){
        return response.currency
      }
      return false
    } catch(error){
      return false
    }
  },
  async getWeather({commit},params){
    try{
      const response = await api(this.$axios).getWeather()
      if (response.status){
        return response.weather
      }
      return false
    }catch(error){
      return false
    }
  },
}

const mutations= {}

const getters = {}

export default {
  actions,
  getters,
  mutations,
  state,
}
