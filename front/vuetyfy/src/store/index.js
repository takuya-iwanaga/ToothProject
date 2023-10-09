import { createStore } from 'vuex'

export const store = createStore({
  state:{
      username: "ddddd"
  },
  mutations:{
    changeNumber(state,payload)
    { state.username =  payload;}
    
  },
  actions:{

  },
})