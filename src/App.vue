<script setup>
/*
=========================================================
* Vue Material Kit 2 - v2.0.0
=========================================================

* Product Page: https://www.creative-tim.com/product/vue-material-kit
* Copyright 2022 Creative Tim (https://www.creative-tim.com)

Coded by www.creative-tim.com

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/
import { RouterView } from "vue-router";
</script>

<template>
  <router-view />
</template>

<style>
.bg-gradient-success {
   background-image: linear-gradient(195deg, rgb(59, 115, 175) 0%, #43A047 100%)!important;

}
.vue3-star-ratings__wrapper {
  margin: 0 !important;
  padding: 0 !important;
  display: inline !important;
  text-align: left !important;
}

.vue3-star-ratings button {
  display: none !important;
}
.vue3-star-ratings {
  display: block !important;
}
</style>
