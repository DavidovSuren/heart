<script setup>
import { onMounted, onUnmounted } from "vue";

//example components
import NavbarDefault from "../../../examples/navbars/NavbarDefault.vue";
import DefaultFooter from "../../../examples/footers/FooterDefault.vue";

//image
import bg1 from "@/assets/img/bg4.webp";

//dep
import Typed from "typed.js";

//sections
import Information from "./Sections/EventsInformation.vue";
import EventsTeam from "./Sections/EventsTeam.vue";

const body = document.getElementsByTagName("body")[0];
//hooks
onMounted(() => {
  body.classList.add("events");
  body.classList.add("bg-gray-200");

  if (document.getElementById("typed")) {
    // eslint-disable-next-line no-unused-vars
    var typed = new Typed("#typed", {
      stringsElement: "#typed-strings",
      typeSpeed: 90,
      backSpeed: 90,
      backDelay: 200,
      startDelay: 500,
      loop: true,
    });
  }
});

onUnmounted(() => {
  body.classList.remove("events");
  body.classList.remove("bg-gray-200");
});
</script>
<template>
  <div class="container position-sticky z-index-sticky top-0">
    <div class="row">
      <div class="col-12">
        <NavbarDefault :sticky="true" />
      </div>
    </div>
  </div>
  <header class="bg-gradient-dark">
    <div class="page-header min-vh-40" :style="{ backgroundImage: `url(${bg1})` }">
    </div> 
  </header>
  <div class="card card-body shadow-xl mx-3 mx-md-6 mt-n6">
    <Information />
    <AboutTeam />
    <Featuring />
    <Newsletter />
  </div>
  <DefaultFooter />
</template>
<style>
h1 {
  font-size: 6em !important;
  text-shadow: 1px 1px 2px gold, 0 0 0em black, 0 0 0.2em black;
}

.page-header {
  min-height: 95vh !important;
}

@media (orientation: portrait) {
  h1 {
    font-size: 1.75em !important;
    margin-top: 6em !important;
    opacity: 0.9;
    text-shadow: 1px 1px 2px rgb(99, 89, 31), 0 0 0em black, 0 0 0.2em black;
  }

  .page-header {
    min-height: 30vh !important;
  }
  .avatar-container {display: none;}
  .card-body.mt-n6 {
    margin-top: 0 !important;
  }
}
</style>