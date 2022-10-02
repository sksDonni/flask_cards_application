import axios from 'axios'
import * as Vue from 'vue'
import Vuex from 'vuex'

const baseURL = "http://192.168.29.210:8000/api"
const authURL = "http://192.168.29.210:8000"

axios.interceptors.request.use(
  request => {
    if(localStorage.getItem('auth_token')){
      request.headers['Authentication-Token'] = localStorage.getItem('auth_token')
    }
    console.log(request.headers)
    return request
  }
)
export const store = new Vuex.Store({
  state: () => ({
    data: [],
    name: "suchith",
    errors: "",
    directories: [],
    cards: [],
    decks: [],
    individualDir:{},
    individualDeck:{},
    individualCard:{},
    cardQueue: [],
    cardQueueStart: 0,
  }),

  mutations:{
    GET_DIRECTORIES(state, payload) {
      state.directories = payload
    }, 
    GET_DIRECTORIES_ERROR(state, payload){
      state.errors = "fetch error"
    }, 
    GET_DIRECTORY_BY_ID(state, payload){
      console.log(payload)
      state.individualDir = payload
    },
    GET_DECK_BY_ID(state, payload){
      console.log(payload)
      state.individualDeck = payload
    },
    GET_CARD_BY_ID(state, payload){
      console.log("commit", payload)
      state.individualCard = payload
    },
    ADD_CARD_BY_DECK_ID(state, payload){
      console.log(payload)
      state.individualDeck.deck_cards.push(payload)
    },
    ADD_DECK_BY_DIR(state, payload){
      console.log(payload)
      state.individualDir.dir_decks.push(payload)
    },
    ADD_DIR(state, payload){
      console.log(payload)
      state.directories.push(payload)
    },
    GET_CARD_BY_ID(state, payload){
      console.log(payload)
      state.individualCard = payload
    },
    EDIT_CARD_BY_ID(state, payload){
      console.log(payload)
    },
    DELETE_DECK_BY_DIR_ID(state, payload){
      console.log(payload)
      let d = state.individualDir.dir_decks
      d = d.filter(a => a.deck_id != payload.deck_id)
      state.individualDir.dir_decks = d
    },
    DELETE_CARD_BY_ID(state, payload){
      console.log(payload)
      let d = state.individualDeck.deck_cards
      d = d.filter(a => a.id != payload.id)
      state.individualDeck.deck_cards = d
    },
    DELETE_DIR_BY_ID(state, payload){
      let d = state.directories
      d = d.filter(a => a.dir_id != payload.dir_id)
      state.directories = d
    }
  },

  actions: {
    async fetchDirectoryById( {commit}, payload ){
      console.log(payload)
      let id = payload.id.toString()
      let response = await axios.get("http://192.168.29.210:8000/api/directory/"+(id))
      let {data} = response
      console.log(data)
      commit("GET_DIRECTORY_BY_ID", data)
      return response
    },

    async fetchDirectories( {commit}, payload ){
      let response = await axios.get("http://192.168.29.210:8000/api/directory")
      let {data} = response
      console.log(data)
      commit("GET_DIRECTORIES", data)
      return response
    },

    async fetchDeckById( {commit}, payload ){
      console.log(payload)
      let id = payload.id.toString()
      let response = await axios.get(baseURL+"/deck/"+id)
      let {data} = response
      console.log(data)
      commit("GET_DECK_BY_ID", data)
      return response
    },

    async fetchCardById( {commit}, payload ){
      console.log(payload)
      let id = payload.id.toString()
      let response = await axios.get(baseURL+"/card/"+id)
      let {data} = response
      console.log(data)
      commit("GET_CARD_BY_ID", data)
      return response
    },

    async addCardByDeck( {commit}, payload){
      console.log(payload)
      let response = await axios.post(baseURL+"/card", payload)
      let {data} = response
      console.log(data)
      commit("ADD_CARD_BY_DECK_ID", data)
      return response
    },

    async updateCardLevel( {commit}, payload){
      console.log(payload)
      let {id} = payload
      let response = await axios.put(baseURL+"/card/"+id, payload)
      console.log(response)
      return response
    },

    async updateDirectoryLevel({commit}, payload){
      console.log(payload)
      let {dir_id} = payload
      let response = await axios.put(baseURL+"/deck/"+dir_id, payload)
      console.log(response)
      return response
    },

    async addDeckByDir( {commit}, payload){
      console.log(payload)
      let {dir_id} = payload
      let response = await axios.post(baseURL+"/deck", payload)
      console.log(response)
      commit("ADD_DECK_BY_DIR", response)
      return response
    },

    async addDir( {commit}, payload){
      console.log(payload)
      let response = await axios.post(baseURL+"/directory", payload)
      commit("ADD_DIR", response)
      return response
    },

    async registerUser( {commit}, payload, router){
      console.log(payload)
      let response = await axios.post(authURL+"/register", payload)
      console.log(response)
      return response
    },

    async loginUser( {commit}, payload){
      console.log(payload)
      let response = await axios.post(authURL+"/login?include_auth_token", payload)
      console.log(response)
      return response
    },

    async fetchCardById( {commit}, payload){
      console.log(payload)
      let id = payload.id.toString()
      let response = await axios.get(baseURL+"/card/"+id)
      let {data} = response
      console.log(data)
      commit("GET_CARD_BY_ID", data)
      return response
    },

    async editCardById( {commit}, payload){
      console.log(payload)
      let id = payload.id.toString()
      let response = await axios.put(baseURL+"/card/"+id, payload)
      let {data} = response
      console.log(data)
      commit("EDIT_CARD_BY_ID", data)
      return response
    },

    async editDeckById( {commit}, payload){
      console.log(payload)
      let id = payload.deck_id.toString()
      let response = await axios.put(baseURL+"/deck/"+id, payload)
      let {data} = response
      console.log(data)
      return response
    },

    async deleteDeckById( {commit}, payload) {
      console.log(payload)
      let {id} = payload
      let response = await axios.delete(baseURL+'/deck/'+id)
      console.log(response)
      let {data} = response
      commit("DELETE_DECK_BY_DIR_ID", data)
      return response
    },

    async deleteCardById( {commit}, payload) {
      console.log(payload)
      let {id} = payload
      let response = await axios.delete(baseURL+'/card/'+id)
      console.log(response)
      let {data} = response
      commit("DELETE_CARD_BY_ID", data)
      return response
    },

    async editDirById( {commit}, payload){
      console.log(payload)
      let id = payload.dir_id.toString()
      let response = await axios.put(baseURL+"/directory/"+id, payload)
      let {data} = response
      console.log(data)
      return response
    },

    async deleteDirById( {commit}, payload) {
      console.log(payload)
      let {id} = payload
      let response = await axios.delete(baseURL+'/directory/'+id)
      console.log(response)
      let {data} = response
      commit("DELETE_DIR_BY_ID", data)
      return response
    },

  },

  getters: {
    directories: state => state.directories
  }

})
