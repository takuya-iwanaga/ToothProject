import { createStore } from 'vuex'

export const store = createStore({
  state:{
      userinfo: ""
  },
  mutations:{
    change_userinfo(state,payload)
    { state.userinfo =  payload;}
    
  },
  actions:{

  },
})