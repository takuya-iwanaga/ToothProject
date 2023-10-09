import { createStore } from 'vuex'

export const store = createStore({
  state:{
      userinfo: ""
  },
  mutations:{
    changeNumber(state,payload)
    { state.userinfo =  payload;}
    
  },
  actions:{

  },
})