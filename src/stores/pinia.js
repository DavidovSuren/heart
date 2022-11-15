import { defineStore } from 'pinia'

export const dateEventStore = defineStore({
  // id is required so that Pinia can connect the store to the devtools
  id: 'dateEvent',
  state: ()=>({ dateEvent: '', mounthEvent: ''})
})