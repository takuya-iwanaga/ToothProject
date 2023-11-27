import { createStore } from 'vuex'
import {ref} from 'vue'

export const store = createStore({
  state:{
      //使用ユーザーの情報
      userinfo: "",
      //予約している情報の一覧
      reservedinfo:"",
      //病院の営業日、営業時間の情報一覧
      reserved_running_list_info:"",
      //追加で予約する月日
      reserving_check_date_info:ref(''),
      //追加で予約する時間
      reserving_check_time_info:ref(''),
      //通院する病院の情報
      hospitalinfo:""
  },
  mutations:{
    //使用ユーザーの情報を更新
    change_userinfo(state,payload)
    { state.userinfo =  payload;},

    //予約している情報の一覧の更新
    change_reservedinfo(state,payload)
    { state.reservedinfo =  payload;},

    //病院の営業日、営業時間の情報一覧の更新
    change_reserved_running_list_info(state,payload)
    { state.reserved_running_list_info =  payload;},

    change_hospitalinfo(state,payload)
    { state.hospitalinfo =  payload;}
    
  },
  actions:{

  },
})