import { defineStore } from 'pinia'

const current = new Date();

export const dateEventStore = defineStore({
  // id is required so that Pinia can connect the store to the devtools
  id: 'dateEvent',
  state: ()=>({ day: current.getDate(), month: current.getMonth()+1 })
})